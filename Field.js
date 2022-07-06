import React, {useState} from "react";
import "./Field.css";
import Task from "./Task";

const Field = () => {
  const [todoBar, setTodoBar] = useState("");
  const [todoArr, setTodoArr] = useState([]);

 
  const handleInputChange = (event) => {
    setTodoBar(event.target.value);
  }

  const handleAddClick = (event) => {
    todoArr.push(event.target.value);
    setTodoArr(todoArr);
    setTodoBar("");
  }

  const handleClearClick = () => {
    setTodoBar("");
  }

 

  return (
    <div>
      <input className = "input" type = "text" value = {todoBar} 
      onChange = {handleInputChange} ></input>
      <button className = "input-btn" onClick={handleAddClick} 
      value = {todoBar}>Add</button>
      <button className = "input-btn" onClick={handleClearClick}>
        Clear</button>
      <div id = "items">
        {todoArr.map((item) => {
          return <Task taskText = {item}/>
          
        })}
      </div>
      
    </div>
    
  )

}

export default Field;