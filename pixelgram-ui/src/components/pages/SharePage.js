import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { Button } from "semantic-ui-react";
import propTypes from "prop-types";
import Toggle from "react-toggle";
import "react-toggle/style.css";

class SharePage extends React.Component {
  constructor(props) {
    super(props);
    this.state = { username: ""};
    this.onChange = this.onChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  //Checks for the change of state and then assigns the form data to the state.
  onChange = (e) =>
    this.setState({ ...this.state, [e.target.name]: e.target.value });

  //Gets the data and sumbits it for a post request
  handleSubmit(event) {
    const { username} = this.state;
    var userid;

    axios.post("http://localhost:5003/userdetails", { username: username })
      .then(function (response) {
        userid = response.data.userid;
        axios.put(`http://localhost:5003/user`, {username: username,userid: userid,password: password,
          })
        .then(function (response) {
            //This is responsible for the page navigation.
            (document.getElementById("status").innerHTML ="Update Password Successfull! You are being redirected to login in 3 seconds."),setTimeout(() => {window.location.replace("/login");}, 3000)
          })
          .catch(function (error) {
            document.getElementById("status").innerHTML = error.message;
          });
      })
      .catch(function (error) {
          document.getElementById("status").innerHTML = error.message;
      });

    event.preventDefault();
  }

  render() {
    return (
      <div align="top">
        <h2>Enter the username you wish to share images</h2>
        <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">
              <b>Username</b>
            </label>
            <br />
            <input
              type="text"
              placeholder="enter username"
              id="username"
              name="username"
              value={this.state.username}
              onChange={this.onChange}
              required
            />
          </div>
          <br />
          <button type="submit" className="button">
            Share
          </button>
        </form>
        <p id="status"></p>
        <Link to="/Landing" className="button">
          Back to Gallery
        </Link>
      </div>
    );
  }
}
export default SharePage;