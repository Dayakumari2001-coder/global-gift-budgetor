#!/bin/bash 
# Define paths to project directory and activate virtual environment
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/backend"
VENV_PATH="${PROJECT_DIR}/venv"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Navigate to the project directory 
cd "${PROJECT_DIR}" || exit 1

# Activate virtual environment
if [ -d "${VENV_PATH}" ]; then
    source "${VENV_PATH}/bin/activate"
    echo "Virtual environment activated at ${VENV_PATH}"
else
    echo "Virtual environment not found at ${VENV_PATH}. Please create it first."
    exit 1
fi

# Execute the python script to update exchange rates
if [ -f "app/services/currency_service.py" ]; then
    python -c "from app.services.currency_service import update_exchange_rates; update_exchange_rates()"
    echo "Exchange rates updated at $(date '+%Y-%m-%d %H:%M:%S') successfully." >> "${SCRIPT_DIR}/rate_log.txt"
else
    echo "Currency service not found. Please check the path."
    exit 1
fi