
// main.jsx - Entry point for the React application.
import React from "react";
import ReactDOM from "react-dom/client";
import app from "./app";
import "./index.css";
import ErrorBoundary from "./ErrorBoundary";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ErrorBoundary fallback={<div>Something went wrong</div>}>
      <app />
    </ErrorBoundary>
  </React.StrictMode>
);