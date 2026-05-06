// main UI controller
import { useState } from "react";
import { getTotal, getRateTime } from "./api/api";
import "./App.css";

import ErrorBoundary from './ErrorBoundary'; 
import ItemForm from "./components/ItemForm";
import ItemList from "./components/ItemList";
import CurrencySelector from "./components/currencySelector";
import React from "react";

function App() {
  const [currency, setCurrency] = useState("home_currency");
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
    <div className="Global gift budgeter">

        <h1>Global Gift Budgeter</h1>
        Welcome Back 
        <ErrorBoundary>
          <ItemForm refresh={refresh} />
          <ItemList refreshFlag={refreshFlag} />

          <CurrencySelector currency={currency} setCurrency={setCurrency} />
        </ErrorBoundary>

        <button onClick={fetchTotal}>Calculate Total</button>
        <h2>Total Budget: {total} {currency}</h2>

        <button onClick={fetchTime}>Show Last Updated</button>
        <p>Last Updated: {time}</p>
      </div>
  );
}

export default App;
