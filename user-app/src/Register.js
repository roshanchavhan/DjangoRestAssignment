import React from "react";
import { useState } from "react";
// import axios from 'axios';

export const Register = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [firstname, setfirstName] = useState("");
  const [lastname, setlastName] = useState("");
  const [dob, setdob] = useState("");
 
  const handleSubmit = (e) => {
    // console.log("form data", e.target.FirstName.value);
    e.preventDefault();
    // axios.post('http://127.0.0.1:8000/register/',{firstname:e.target.FirstName.value,lastname:e.target.LastName.value, email:e.target.Email.value,dob:e.target.DOB.value,pass:e.target.Password.value,})
    // .then((response) => response.json())
    // .catch((err) => console.log(err));
    fetch("http://127.0.0.1:8000/register/", {
     
    // Adding method type
    method: "POST",
     
    // Adding body or contents to send
    body: JSON.stringify({
      email:e.target.Email.value,
      password:e.target.Password.value,
      first_name:e.target.FirstName.value,
      last_name:e.target.LastName.value,
      date_of_birth:e.target.DOB.value,
      
    }),
     
    // Adding headers to the request
    headers: {
        "Content-type": "application/json; charset=UTF-8",
      
    }
})
 
// Converting to JSON
.then(response => response.json())
  };

  return (
    <div className="userClass">
      <form className="register-form" onSubmit={handleSubmit}>
        <label htmlFor="FirstName">First Name</label>
        <input value={firstname} onChange={(e)=>setfirstName(e.target.value)} type="text" placeholder="First Name" name="FirstName" id="firstname" required />
        <label htmlFor="LastName">Last Name</label>
        <input value={lastname} onChange={(e)=>setlastName(e.target.value)} type="text" placeholder="Last Name" name="LastName" id="lastname" required/>
        <label htmlFor="DOB">Date Of Birth</label>
        <input value={dob} onChange={(e)=>setdob(e.target.value)} type="date" placeholder="Enter Your BirthDate" name="DOB" id="dob" required/>
        <label htmlFor="Email">Email</label>
        <input value={email} onChange={(e)=>setEmail(e.target.value)} type="email" placeholder="Enter Your Mail" name="Email" id="email" required/>
        <label htmlFor="Password">Password</label>
        <input value={pass} onChange={(e)=>setPass(e.target.value)} type="password" placeholder="Enter Your Password" name="Password" id="password" required/>
        <button type="submit">Register</button>
      </form>
      <p>
        Already Have An Account <button className="link-btn" onClick={()=>props.onFormSwitch('Login')}>Log In Here</button>
      </p>
    </div>
  );
};
