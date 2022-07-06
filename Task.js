import React, {useState} from "react";
import "./Task.css";


const Task = (props) => {
  const [isRemoved, setIsRemoved] = useState(false);
  const [doneList, setDoneList] = useState([]);

  const manageRemoveClick = () => {
    setIsRemoved(true);
  }
  
  

  if (!isRemoved) {
    return (
      <div id = "task-box">
        <div id= "task-text">
          {props.taskText}
        </div>
        <button className="manage-x" onClick={manageRemoveClick}>
          X
        </button>
        
      </div>
    )
  }
  
}

export default Task;