import { useEffect, useState } from "react";
import { getItems, deleteItem, editItem } from "../api/api";

function ItemList() {
  const [items, setItems] = useState([]);
  const [editId, setEditId] = useState(null);
  const [editData, setEditData] = useState({
    item_name: "",
    foreign_price: "",
    currency: "",
  });

  const load = async () => {
    try {
      const data = await getItems();
      setItems(data);
    } catch (error) {
      console.error("Failed to load items:", error);
    }
  };

  const remove = async (id) => {
    try {
      await deleteItem(id);
      load();
    } catch (error) {
      console.error("Failed to delete item:", error);
    }
  };

  const startEdit = (item) => {
  setEditId(item.id);
  setEditData({
    item_name: item.item_name,
    foreign_price: item.foreign_price,
    currency: item.currency,
  });
};

const handleChange = (e) => {
  const { name, value } = e.target;
  setEditData((prev) => ({
    ...prev,
    [name]: value,
  }));
};

const saveEdit = async () => {
  if (!editId) {
    console.error("No item ID selected for update");
    return;
  }
  try {
    await editItem(editId, editData);
    setEditId(null);
    load();
  } catch (error) {
    // Check if the server provided specific validation errors
    if (error.response && error.response.status === 422) {
      console.error("Validation Errors:", error.response.data);
      alert(`Update failed: ${JSON.stringify(error.response.data.errors || error.response.data)}`);
    } else {
      console.error("Failed to update item:", error);
    }
  }
};

const cancelEdit = () => {
  setEditId(null);
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
        {items.map((i, idx) => (
          <tr key={i.id}>
            <td>{idx + 1}</td>

            {/* ITEM NAME */}
            <td>
              {editId === i.id ? (
                <input
                  name="item_name"
                  value={editData.item_name}
                  onChange={handleChange}
                />
              ) : (
                i.item_name
              )}
            </td>

            {/* PRICE */}
            <td>
              {editId === i.id ? (
                <input
                  name="foreign_price"
                  value={editData.foreign_price}
                  onChange={handleChange}
                />
              ) : (
                i.foreign_price
              )}
            </td>

            {/* CURRENCY */}
            <td>
              {editId === i.id ? (
                <input
                  name="currency"
                  value={editData.currency}
                  onChange={handleChange}
                />
              ) : (
                i.currency
              )}
            </td>

            {/* ACTION */}
            <td>
              {editId === i.id ? (
                <>
                  <button onClick={saveEdit}>Save</button>
                  <button onClick={cancelEdit}>Cancel</button>
                </>
              ) : (
                <>
                  <button onClick={() => startEdit(i)}>Edit</button>
                  <button onClick={() => remove(i.id)}>Delete</button>
                </>
              )}
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ItemList;