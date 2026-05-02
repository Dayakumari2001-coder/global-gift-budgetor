// form to add new item
import { useState } from "react";
import { addItem } from "../api/api";
import Select from "react-select";
import cc from "currency-codes";

function ItemForm({ refresh }) {
  const [item, setItem] = useState("");
  const [price, setPrice] = useState("");
  const [currency, setCurrency] = useState("");
  const currencyOptions = cc.codes().map(code => ({ value: code, label: `${code} -${cc.currencies(code).name}` }));

  const submit = async () => {
    await addItem({
      user_id: 1,
      item_name: item,
      price: parseFloat(price),
      currency
    });

    setItem("");
    setPrice("");
    refresh(); // reload table
  };

  return (
    <div>
      <h3>Add Item</h3>

      <input
        placeholder="Item"
        value={item}
        onChange={(e) => setItem(e.target.value)}
      />

      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <Select
        value={currencyOptions.find(option => option.value === currency)}
        onChange={(selectedOption) => setCurrency(selectedOption.value)}
        options={currencyOptions}
        placeholder="Select Currency"
        isClearable
        isSearchable
      />

      <button onClick={submit}>Add</button>
    </div>
  );
}

export default ItemForm;