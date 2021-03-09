import io
import os
import tempfile
import zipfile

from flask import jsonify, send_file
import requests

from config import SCOPES, CLIENT_SECRET_FILE_PATH, APP_NAME, CONNECT_TO, DRIVE_VERSION, IMAGE_SERVICE_URL

from apiclient.http import MediaIoBaseDownload, MediaIoBaseUpload
import googleapiclient.discovery

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import httplib2

from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

MIMETPES = dict(**{
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg'
})

HEADERS = dict(**{
    'Content-type': 'application/json'
})

def drive_auth_creds():
    cwd_dir = os.getcwd()
    credential_dir = os.path.join(cwd_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'google-drive-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE_PATH, SCOPES)
        flow.user_agent = APP_NAME
        credentials = tools.run_flow(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def getDriveService():
    try:
        credentials = drive_auth_creds()
        http = credentials.authorize(httplib2.Http())
        return googleapiclient.discovery.build(CONNECT_TO, DRIVE_VERSION, http=http)
    except Exception as e:
        print('Error in connecing to google drive with provided creds.')
        print(e)
        raise Exception('Google Drive connection error')


def save_image(drive_api, file_name, mime_type, file_data):
    body = {
        'name': file_name,
        'tittle': file_name,
        'mimeType': mime_type,
    }
    media_body = MediaIoBaseUpload(file_data, mimetype=mime_type, resumable=True)
    image_id = drive_api.files().create(body=body, media_body=media_body, fields='id').execute()

    return image_id

def files_to_be_uploaded(files, user_id):
    drive_api = getDriveService()
    image_ids = []
    failed_uploads = []
    for file in files:
        filename = secure_filename(file.filename)
        if filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
            failed_uploads.append({'image_name': filename, 'reason': 'Not a valid extension'})
        
        mimetype = MIMETPES[filename.rsplit('.', 1)[1].lower()]
        
        file_data = tempfile.TemporaryFile()
        ch = file.read()
        file_data.write(ch)
        file_data.seek(0)

        try:
            image_id = save_image(drive_api, user_id+'_'+filename, mimetype, file_data)
            image_ids.append(image_id)
        except Exception as e:
            failed_uploads.append({'image_name': filename, 'reason': e})
    
    # Send this information to image service to store the user-image mapping
    data = {
        "userid": user_id,
        "imageids": image_ids
    }

    response = requests.post(IMAGE_SERVICE_URL, data=data, headers=HEADERS)

    if response.status_code == 200:
        print('Details posted successfully to image service')

    print(user_id)
    print(image_ids)
    print(failed_uploads)
    
    return jsonify(
        userid= user_id,
        fails=failed_uploads,
        success=image_ids
    ), 200

def get_file_data_drive(drive_api, file_id):
    try:
        request = drive_api.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while done is False:
            status, done = downloader.next_chunk()

        fh.seek(0)
        return fh
    except Exception as e:
        raise Exception(e)

def get_file_meta_data_drive(drive_api, file_id, fields):
    try:
        metadata = drive_api.files().get(fields=fields, fileId=file_id).execute()
        return metadata
    except Exception as e:
        raise Exception(e)


def view_file(file_id):

    try:
        drive_api = getDriveService()
        metadata = get_file_meta_data_drive(
            drive_api=drive_api,
            fields="name,mimetype",
            file_id=file_id
        )
        print(metadata)

        filedata = get_file_data_drive(drive_api=drive_api, file_id=file_id)
        return send_file(
            filedata,
            attachment_filename=metadata['name'],
            mimetype=metadata['mimeType']
        )
    except Exception as e:
        return jsonify(
            message='Failed',
            error=e
        ), 500

def download_multiple_files(fileids):
    try:
        drive_api = getDriveService()
        zip_file = BytesIO()
        with zipfile.ZipFile(zip_file, 'w', compression= zipfile.ZIP_STORED) as zf:
            for file_id in fileids:
                filedata = get_file_data_drive(drive_api=drive_api, file_id=file_id)
                metadata = get_file_meta_data_drive(
                    drive_api=drive_api,
                    fields="name",
                    file_id=file_id
                )
                zip_info_data = zipfile.ZipInfo(metadata['name'])
                zf.writestr(data, filedata)
        zip_file.seek(0)
        return send_file(
            zip_file,
            attachment_filename=images.zip,
            as_attachment= True
        )
    except Exception as e:
        return jsonify(
            message='Download Failed',
            error = e
        ), 500