import React from "react";
import { useState } from "react";

export const Login = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPass] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:8000/login/", {
     
    // Adding method type
    method: "POST",
     
    // Adding body or contents to send
    body: JSON.stringify({
      email:e.target.Email.value,
      password:e.target.Password.value,
    }),
     
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8"
    }
})
 
// Converting to JSON
.then(response => 
  response.json())
 
  };

  return (
    <div className="userClass">
      <form className="login-form" onSubmit={handleSubmit}>
        <label htmlFor="Email">Email</label>
        <input value={ email } onChange={(e) => setEmail(e.target.value)} type="email" placeholder="Enter Your Mail" name="Email" id="email" required/>
        <label htmlFor="Password">Password</label>
        <input value={ password } onChange={(e) => setPass(e.target.value)} type="password" placeholder="Enter Your Password" name="Password" id="password" required/>
        <button type="submit">Log In</button>
      </form>
      <p>Don't Have An Account <button className="link-btn" onClick={() => props.onFormSwitch("Register")}>Register Here </button> </p>
    </div>
  );
};
