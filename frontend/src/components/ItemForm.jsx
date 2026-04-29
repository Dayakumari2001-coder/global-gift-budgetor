// form to add new item
import { useState } from "react";
import { addItem } from "../api/api";

function ItemForm({ refresh }) {
  const [item, setItem] = useState("");
  const [price, setPrice] = useState("");
  const [currency, setCurrency] = useState("USD");

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

      <select onChange={(e) => setCurrency(e.target.value)}>
        <option>USD</option>
        <option>EUR</option>
      </select>

      <button onClick={submit}>Add</button>
    </div>
  );
}

export default ItemForm;