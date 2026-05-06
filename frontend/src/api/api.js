import axios from 'axios'; 
// Frontend API utility for Global Gift Budgetor
const BASE_URL = 'http://localhost:8000'; // Ensure this matches your BACKEND port, not Vite's port


// Add item to wishlist
export const addItem = (data) =>
  fetch(BASE_URL + "/add-item", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

// Get all items
export const getItems = () =>
  fetch(BASE_URL + "/items")
    .then(res => {
      if (!res.ok) throw new Error('Failed to fetch items');
      return res.json();
    })
    .catch(err => {
      console.error("Fetch error:", err);
      return [];
    });

// Delete item
export const deleteItem = (id) =>
  fetch(BASE_URL + `/delete-item/${id}`, { method: "DELETE" });

// Edit item
export const editItem = async (id, data) => {
  return axios.put(BASE_URL + `/items/${id}`, data);
  
  try {  
    await editItem(editId, editData); 
      setEditId(null);
      load(); 
  } 
    catch (error) {
      console.error("Failed to update item:", error);
    }
};

// Get total budget
export const getTotal = (currency) =>
  fetch(BASE_URL + `/total/${currency}`)
    .then(res => {
      if (!res.ok) throw new Error('Failed to fetch total');
      return res.json();
    })
    .catch(err => {
      console.error("Fetch error:", err);
      return { total: 0 };
    });

// Get last updated time for exchange rates
export const getRateTime = (currency) =>
  fetch(BASE_URL + `/rate-time/${currency}`)
    .then(res => res.json())
    .catch(err => {
      console.error("Fetch error:", err);
      return { last_updated: null };
    });
