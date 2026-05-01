// main UI controller
import { useState } from "react";
import { getTotal, getRateTime } from "./api/api";
import "./App.css";

import ItemForm from "./components/ItemForm";
import ItemList from "./components/ItemList";
import CurrencySelector from "./components/CurrencySelector";

function App() {
  const [currency, setCurrency] = useState("INR");
  const [total, setTotal] = useState(0);
  const [time, setTime] = useState("");
  const [refreshFlag, setRefreshFlag] = useState(0);

  const refresh = () => {
    setRefreshFlag(prev => prev + 1);
  };

  const fetchTotal = async () => {
    const data = await getTotal(currency);
    setTotal(data.total);
  };

  const fetchTime = async () => {
    const data = await getRateTime(currency);
    setTime(data.last_updated);
  };

  return (
    <div>
      <h1>Global Gift Budgeter</h1>

      <ItemForm refresh={refresh} />
      <ItemList refreshFlag={refreshFlag} />

      <CurrencySelector currency={currency} setCurrency={setCurrency} />

      <button onClick={fetchTotal}>Calculate Total</button>
      <h2>Total: {total} {currency}</h2>

      <button onClick={fetchTime}>Show Last Updated</button>
      <p>Last Updated: {time}</p>
    </div>
  );
}

export default App;
