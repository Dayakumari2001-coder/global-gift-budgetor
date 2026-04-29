import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    // Simulate an API call or other side effect
    const [data, setData] = useState([]);
    useEffect(() => {
      fetch('https://127.0.0.1:8000/transactions')
        .then(response => response.json())
        .then(data => setData(data))
        .catch(error => console.error('Error fetching data:', error));
    }, []);
    return (
      <div>
        <h1>Transactions</h1>
        {data.map(item => (
          <div key={item.id}>
            <p>{item.title} - ₹{item.amount}</p>
          </div>
        ))}
      </div>
    );
  }, [])

}

export default App
