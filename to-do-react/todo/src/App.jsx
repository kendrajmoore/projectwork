import { useState } from 'react'
import './App.css'

function App() {
  const [todos, setTodos] = useState([]);
  const [inputText, setInputText] = useState('');

  const addToDos = (e) => {
    e.preventDefault();
    setTodos([...todos, { todo: inputText, completed: false}]);
    setInputText('');
  }

  const deleteToDos = (index) => {
    const updatedToDos = todos.filter((_, i) => i !== index);
    setTodos(updatedToDos)
  }

  const markComplete = (index) => {
    const updatedToDos = [...todos];
    updatedToDos[index].completed = !updatedToDos[index].completed;
    setTodos(updatedToDos);
  }

  return (
    <>
      <h1>To Do List</h1>
      <form onSubmit={addToDos}>
        <input 
          id="formInput" 
          type="text" 
          placeholder="Enter To Do" 
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}/>
        <button id="btn" type="submit">Submit</button>
      </form>
      <ul id="list">
        {todos.map((todo, index) => (
          <li key={index}> 
            <input 
              type="checkbox"
              checked={todo.completed}
              onChange={() => markComplete(index)}
              /><label className={todo.completed ? 'completed' : ''}>{todo.todo}</label>
              <button id="delete" onClick={() => deleteToDos(index)}>Delete</button>
              </li>
        ))}
      </ul>
    </>
  )
}

export default App;
