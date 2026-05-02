// dropdown to select home currency
import {useState} from "react";
import Select from "react-select"; 
import cc from "currency-codes";

function CurrencyComponent(){
  const [currency, setCurrency] = useState("");
  const [total, setTotal] = useState(null);
  const [errorMessage, setErrorMessage]= useState("");

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
      if(!response.ok) {
        //If status is 400 or500, show error message from backend or default message
        setErrorMessage(data.total ||"Error fetching total budget.");
      } else {
        setTotal(data.total);
      }
    } catch (error) {
      setErrorMessage("Network error: Could not reach the server.");
    }
  };

  const currencyOptions = cc.codes().map(code => ({ value: code, label: `${code} -${cc.currencies(code).name}` }));
  return (
    <div>
      <h3>Select Currency</h3>
      <Select
        value={currencyOptions.find(option => option.value === currency)}
        onChange={(selectedOption) => setCurrency(selectedOption.value)}
        options={currencyOptions}
        placeholder="Type or select currency"
        isClearable
        isSearchable
      />
      <button onClick={fetchTotal}>Get Total</button>
      
      {/*Conditionally show the error message*/}
      {errorMessage && (
        <div style={{color: "red",marginTop: "10px", fontWeight: "bold"}}>{errorMessage}</div>
      )}

      {total !== null && <p>Total Budget: {total} {currency}</p>}
    </div>
  );
}

export default CurrencySelector;