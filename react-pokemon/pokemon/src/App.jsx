import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  let url = `https://pokeapi.co/api/v2/pokemon/`
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const randomNumbers = [];
  for (let i = 0; i < 10; i++) {
      const randomNumber = Math.floor(Math.random() * 200) + 1;
      randomNumbers.push(randomNumber);
  }
  useEffect(() => {
    async function fetchData(){
      try{
        const newData = [];
        for(const num of randomNumbers){
          let newUrl = url + num;
          const response = await axios.get(newUrl);
          newData.push(response.data);
          console.log(newData)
        }
        setData(newData);
        setLoading(false);
      } catch (error){
        console.error('Error fetching data');
        setLoading(false);
      }
    }
    fetchData();
  }, []);
  
 
  return (
    <>
     <h1>Get Pokemon</h1>
     {loading ? (<p>Loading...</p>) : (
        <div className='card-container'>
          {data.map((item) => (
            <div key={item.id} className='card'>
              <img src={item.sprites.back_default}/>
              <h2>{item.name}</h2>
              <p>Type: {item.types[0].type.name}</p>
              <p>Base Experience: {item.base_experience}</p>
            </div>
          ))}
      </div>
     )}
      <form>
        <button id="btn">Submit</button>
      </form>
    </>
  )
}

export default App
