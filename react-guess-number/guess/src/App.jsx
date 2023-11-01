import { useState } from 'react'
import './App.css'

const randomNumber = Math.floor(Math.random() * 100) + 1;
console.log(randomNumber)

function App() {
  const [inputText, setInputText] = useState('');
  const [result, setResult] = useState('')

  const generateNum = (e) => {
    e.preventDefault();
    const userGuess = Number(inputText);
    if(isNaN(userGuess)){
      setResult("Please enter a valid number")
    } else if(userGuess === randomNumber){
      setResult("Congrats you guess the right number")
    } else if (userGuess > randomNumber){
      setResult("You guessed too high")
    } else {
      setResult("You guessed too low")
    }
    setInputText('');
  }

  return (
    <>
      <h1>Guess A Number</h1>
      <form onSubmit={generateNum}>
        <input 
          id="formInput" 
          type="text" value={inputText} 
          placeholder="Enter a number 1-100"
          onChange={(e) =>setInputText(e.target.value)}/>
        <button id="btn">Sumbit</button>
        <p id="result">{result}</p>
      </form>
      
    </>
  )
}

export default App
