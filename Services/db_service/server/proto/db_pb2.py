# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: db.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='db.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\220\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08\x64\x62.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"-\n\x0eStatusResponse\x12\x1b\n\x06status\x18\x01 \x01(\x0e\x32\x0b.Statuscode\"\\\n\x07Session\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06userId\x18\x02 \x01(\t\x12.\n\nexpireTime\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb5\x01\n\x10ImageUserDetails\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0f\n\x07imageId\x18\x02 \x01(\t\x12\x17\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x07.Format\x12,\n\x08\x64\x61teTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\x12\x14\n\x0clocationName\x18\x07 \x01(\t\"\xa1\x01\n\x0cImageDetails\x12\x0f\n\x07imageId\x18\x01 \x01(\t\x12\x17\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x07.Format\x12,\n\x08\x64\x61teTime\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01\x12\x14\n\x0clocationName\x18\x07 \x01(\t\"P\n\x0bUserDetails\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"9\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x1c\n\x0bqueryString\x12\r\n\x05value\x18\x01 \x01(\t*%\n\x06\x46ormat\x12\x08\n\x04JPEG\x10\x00\x12\x07\n\x03PNG\x10\x01\x12\x08\n\x04WEBP\x10\x02*&\n\nStatuscode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32\xe1\x03\n\x0f\x44\x61tabaseService\x12;\n\x12UpdateImageDetails\x12\r.ImageDetails\x1a\x16.google.protobuf.Empty\x12!\n\nCreateUser\x12\x05.User\x1a\x0c.UserDetails\x12\x36\n\x0eupdateUserName\x12\x0c.UserDetails\x1a\x16.google.protobuf.Empty\x12:\n\x12UpdateUserPassword\x12\x0c.UserDetails\x1a\x16.google.protobuf.Empty\x12/\n\x0b\x43reateImage\x12\x11.ImageUserDetails\x1a\r.ImageDetails\x12.\n\x0fGetImageDetails\x12\x0c.queryString\x1a\r.ImageDetails\x12-\n\x16GetUserPasswordByEmail\x12\x0c.queryString\x1a\x05.User\x12)\n\x13SessionTokenForUser\x12\x08.Session\x1a\x08.Session\x12?\n\x1bValidateSessionTokenForUser\x12\x08.Session\x1a\x16.google.protobuf.EmptyB\x03\x90\x01\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])

_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='Format',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='JPEG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PNG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WEBP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=734,
  serialized_end=771,
)
_sym_db.RegisterEnumDescriptor(_FORMAT)

Format = enum_type_wrapper.EnumTypeWrapper(_FORMAT)
_STATUSCODE = _descriptor.EnumDescriptor(
  name='Statuscode',
  full_name='Statuscode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=773,
  serialized_end=811,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

Statuscode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
JPEG = 0
PNG = 1
WEBP = 2
SUCCESS = 0
FAILURE = 1



_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='StatusResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=119,
)


_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessionId', full_name='Session.sessionId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userId', full_name='Session.userId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='expireTime', full_name='Session.expireTime', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=213,
)


_IMAGEUSERDETAILS = _descriptor.Descriptor(
  name='ImageUserDetails',
  full_name='ImageUserDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='ImageUserDetails.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='imageId', full_name='ImageUserDetails.imageId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='ImageUserDetails.format', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='ImageUserDetails.dateTime', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='ImageUserDetails.latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='ImageUserDetails.longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locationName', full_name='ImageUserDetails.locationName', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=216,
  serialized_end=397,
)


_IMAGEDETAILS = _descriptor.Descriptor(
  name='ImageDetails',
  full_name='ImageDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='imageId', full_name='ImageDetails.imageId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='format', full_name='ImageDetails.format', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='ImageDetails.dateTime', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='ImageDetails.latitude', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='ImageDetails.longitude', index=4,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locationName', full_name='ImageDetails.locationName', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=561,
)


_USERDETAILS = _descriptor.Descriptor(
  name='UserDetails',
  full_name='UserDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserDetails.userId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='UserDetails.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='UserDetails.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='UserDetails.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=643,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='User.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='User.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=645,
  serialized_end=702,
)


_QUERYSTRING = _descriptor.Descriptor(
  name='queryString',
  full_name='queryString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='queryString.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=704,
  serialized_end=732,
)

_STATUSRESPONSE.fields_by_name['status'].enum_type = _STATUSCODE
_SESSION.fields_by_name['expireTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_IMAGEUSERDETAILS.fields_by_name['format'].enum_type = _FORMAT
_IMAGEUSERDETAILS.fields_by_name['dateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_IMAGEDETAILS.fields_by_name['format'].enum_type = _FORMAT
_IMAGEDETAILS.fields_by_name['dateTime'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['ImageUserDetails'] = _IMAGEUSERDETAILS
DESCRIPTOR.message_types_by_name['ImageDetails'] = _IMAGEDETAILS
DESCRIPTOR.message_types_by_name['UserDetails'] = _USERDETAILS
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['queryString'] = _QUERYSTRING
DESCRIPTOR.enum_types_by_name['Format'] = _FORMAT
DESCRIPTOR.enum_types_by_name['Statuscode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATUSRESPONSE,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:StatusResponse)
  })
_sym_db.RegisterMessage(StatusResponse)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), {
  'DESCRIPTOR' : _SESSION,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:Session)
  })
_sym_db.RegisterMessage(Session)

ImageUserDetails = _reflection.GeneratedProtocolMessageType('ImageUserDetails', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEUSERDETAILS,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:ImageUserDetails)
  })
_sym_db.RegisterMessage(ImageUserDetails)

ImageDetails = _reflection.GeneratedProtocolMessageType('ImageDetails', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEDETAILS,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:ImageDetails)
  })
_sym_db.RegisterMessage(ImageDetails)

UserDetails = _reflection.GeneratedProtocolMessageType('UserDetails', (_message.Message,), {
  'DESCRIPTOR' : _USERDETAILS,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:UserDetails)
  })
_sym_db.RegisterMessage(UserDetails)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)

queryString = _reflection.GeneratedProtocolMessageType('queryString', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSTRING,
  '__module__' : 'db_pb2'
  # @@protoc_insertion_point(class_scope:queryString)
  })
_sym_db.RegisterMessage(queryString)


DESCRIPTOR._options = None

_DATABASESERVICE = _descriptor.ServiceDescriptor(
  name='DatabaseService',
  full_name='DatabaseService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=814,
  serialized_end=1295,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateImageDetails',
    full_name='DatabaseService.UpdateImageDetails',
    index=0,
    containing_service=None,
    input_type=_IMAGEDETAILS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='DatabaseService.CreateUser',
    index=1,
    containing_service=None,
    input_type=_USER,
    output_type=_USERDETAILS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='updateUserName',
    full_name='DatabaseService.updateUserName',
    index=2,
    containing_service=None,
    input_type=_USERDETAILS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUserPassword',
    full_name='DatabaseService.UpdateUserPassword',
    index=3,
    containing_service=None,
    input_type=_USERDETAILS,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateImage',
    full_name='DatabaseService.CreateImage',
    index=4,
    containing_service=None,
    input_type=_IMAGEUSERDETAILS,
    output_type=_IMAGEDETAILS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetImageDetails',
    full_name='DatabaseService.GetImageDetails',
    index=5,
    containing_service=None,
    input_type=_QUERYSTRING,
    output_type=_IMAGEDETAILS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserPasswordByEmail',
    full_name='DatabaseService.GetUserPasswordByEmail',
    index=6,
    containing_service=None,
    input_type=_QUERYSTRING,
    output_type=_USER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SessionTokenForUser',
    full_name='DatabaseService.SessionTokenForUser',
    index=7,
    containing_service=None,
    input_type=_SESSION,
    output_type=_SESSION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ValidateSessionTokenForUser',
    full_name='DatabaseService.ValidateSessionTokenForUser',
    index=8,
    containing_service=None,
    input_type=_SESSION,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATABASESERVICE)

DESCRIPTOR.services_by_name['DatabaseService'] = _DATABASESERVICE

DatabaseService = service_reflection.GeneratedServiceType('DatabaseService', (_service.Service,), dict(
  DESCRIPTOR = _DATABASESERVICE,
  __module__ = 'db_pb2'
  ))

DatabaseService_Stub = service_reflection.GeneratedServiceStubType('DatabaseService_Stub', (DatabaseService,), dict(
  DESCRIPTOR = _DATABASESERVICE,
  __module__ = 'db_pb2'
  ))


# @@protoc_insertion_point(module_scope)
