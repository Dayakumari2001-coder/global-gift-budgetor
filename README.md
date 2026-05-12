# Global Gift Budgetor

Global Gift Budgetor is a full-stack project for tracking gift items, prices, and currency conversion. The backend provides APIs for storing wishlist items and calculating totals in a target currency, while the frontend is a React/Vite application for adding items and selecting currencies.

## Repository Structure

- `backend/` - Python backend application
  - `app/` - FastAPI app, routes, services, and database logic
  - `requirements.txt` - Python dependencies for the backend
- `frontend/` - React frontend application
  - `src/` - React source files and components
  - `package.json` - frontend dependencies and scripts
- `database/` - SQL schema, seed data, and test SQL files

## Backend Setup

1. Create and activate a Python virtual environment in `backend/`:
   ```bash
   cd backend
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in a `.env` file (if not already present):
   ```env
   DATABASE_URL=mysql+pymysql://root:password@localhost/gift_budgeter
   EXCHANGE_RATE_API_KEY=your_api_key_here
   ```

4. Start the backend server:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Frontend Setup

1. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. If not already installed, add required frontend packages:
   ```bash
   npm install react-select currency-codes
   ```

3. Start the frontend in development mode:
   ```bash
   npm run dev
   ```

4. Open the local Vite URL shown in the terminal, typically `http://localhost:5173`.

## Database

- The project expects a MySQL database for the backend.
- The backend currently connects using the credentials in `backend/app/db.py`.
- Use SQL files in `database/` to create schema and seed sample data.

## Notes

- Backend routes are defined in `backend/app/routes/`.
- Currency conversion logic is handled by `backend/app/services/currency_service.py`.
- The frontend uses React components in `frontend/src/components/` and calls backend APIs.

## Troubleshooting

- If the frontend imports `react-select` or `currency-codes`, ensure those packages are installed.
- If the backend cannot connect to the database, verify MySQL credentials and database name.
- If API rate fetching fails, check the `EXCHANGE_RATE_API_KEY` and the exchange API endpoint.
