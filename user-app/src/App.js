import React, {useState} from "react";
import { Login } from "./Login";
import "./App.css";
import { Register } from "./Register";
// import ReactDOM from "react-dom/client";
// import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  const [currentForm, setcurrentForm]= useState('Login')

  const toggleForm = (formName)=>{
    setcurrentForm(formName);
  }
  return (
    <div className="App">
     {
      currentForm === 'Login'?<Login onFormSwitch={toggleForm}/> : <Register onFormSwitch={toggleForm}/>
     }
    </div>
  );
}

export default App;
