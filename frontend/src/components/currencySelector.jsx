// dropdown to select home currency
function CurrencySelector({ currency, setCurrency }) {
  return (
    <div>
      <h3>Select Currency</h3>

      <select value={currency} onChange={(e) => setCurrency(e.target.value)}>
        <option>INR</option>
        <option>USD</option>
        <option>EUR</option>
      </select>
    </div>
  );
}

export default CurrencySelector;