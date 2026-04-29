import { useEffect, useState } from "react";
import { getItems, deleteItem } from "../api/api";

function ItemList() {
  const [items, setItems] = useState([]);

  const load = async () => {
    const data = await getItems();
    setItems(data);
  };

  const remove = async (id) => {
    await deleteItem(id);
    load();
  };

  useEffect(() => {
    load();
  }, []);

  return (
    <table border="1">
      <thead>
        <tr>
          <th>ID</th>
          <th>Item</th>
          <th>Price</th>
          <th>Currency</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>
        {items.map((i) => (
          <tr key={i.id}>
            <td>{i.id}</td>
            <td>{i.item_name}</td>
            <td>{i.foreign_price}</td>
            <td>{i.currency}</td>
            <td>
              <button onClick={() => remove(i.id)}>Delete</button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ItemList;