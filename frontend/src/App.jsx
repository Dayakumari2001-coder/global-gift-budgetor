import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [total, setTotal] = useState(0)

  useEffect(() => {
    fetch('http://127.0.0.1:8000/total')
      .then(response => response.json())
      .then(data => setTotal(data.total_inr))
      .catch(error => console.error('Error fetching total:', error));
  }, [])

  return (
    <div>
      <h1>Gift Budget Total</h1>
      <p>Total in INR: ₹{total}</p>
    </div>
  );
}

export default App
