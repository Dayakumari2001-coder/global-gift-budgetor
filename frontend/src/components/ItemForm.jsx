// form to add new item
import { useState } from "react";
import { addItem } from "../api/api";
import cc from "currency-codes";
import axios from 'axios';

function ItemForm({ refresh }) {
  const [item, setItem] = useState("");
  const [price, setPrice] = useState("");
  const [currency, setCurrency] = useState("");
  const currencyOptions = cc.codes().map(code => {
    const currencyInfo = cc.code(code);
    return {
      value: code,
      label: `${code} - ${currencyInfo?.currency || 'unknown currency'}`
    };
  });

  const submit = async () => {
    try {
      await addItem({
        item_name: item,
        price: parseFloat(price),
        currency
      });

      setItem("");
      setPrice("");
      refresh(); // reload table
    } catch (error) {
      console.error("Failed to add item:", error);
    }
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

      <select value={currency} onChange={(e) => setCurrency(e.target.value)}>
        <option value="">Select Currency</option>
        {currencyOptions.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>

      <button onClick={submit}>Add</button>
    </div>
  );
}

export default ItemForm;