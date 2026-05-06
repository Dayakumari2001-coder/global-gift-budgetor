// dropdown to select home currency
import { useState } from "react"
import cc from "currency-codes";

function CurrencySelector() {
  const [currency, setCurrency] = useState("USD");
  const [total, setTotal] = useState(null);

  const fetchTotal = async () => {
    try {
      const response = await fetch("http://localhost:8000/get-total", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ home_currency: currency })
      });

      const data = await response.json();
      if (!response.ok) {
        console.error(data.detail || "Error fetching total budget.");
      } else {
        setTotal(data.total);
      }
    } catch (error) {
      console.error("Network error: Could not reach the server.", error);
    }
  };

  const currencyOptions = cc.codes().map(code => {
    const currencyInfo = cc.code(code);
    return {
      value: code,
      label: `${code} - ${currencyInfo?.currency || 'unknown currency'}`
    };
  });

  return (
    <div>
      <h3>Select Currency</h3>
      <select value={currency} onChange={(e) => setCurrency(e.target.value)}>
        <option value="">Select currency</option>
        {currencyOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
      <button onClick={fetchTotal}>Get Total</button>

      {total !== null && <p>Total Budget: {total} {currency}</p>}
    </div>
  );
}

export default CurrencySelector;