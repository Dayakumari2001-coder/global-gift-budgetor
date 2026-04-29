// base API URL
const BASE = "http://127.0.0.1:8000";

// add item
export const addItem = (data) =>
  fetch(BASE + "/add-item", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(data)
  });

// get all items
export const getItems = () =>
  fetch(BASE + "/items").then(res => res.json());

// delete item
export const deleteItem = (id) =>
  fetch(BASE + `/delete-item/${id}`, { method: "DELETE" });

// get total
export const getTotal = (currency) =>
  fetch(BASE + `/total/${currency}`).then(res => res.json());

// get last updated time
export const getRateTime = (currency) =>
  fetch(BASE + `/rate-time/${currency}`).then(res => res.json());
