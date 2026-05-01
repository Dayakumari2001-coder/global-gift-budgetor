#!/bin/bash 
#define paths project directory and activate virtual environment
PROJECT_DIR= "/path/to/your/project/backend"
VENV_PATH= "/path/to/your/project/backend/venv"
# Navigate to the project directory 
cd "${PROJECT_DIR}"
# activate virtual environment
if [ -f "${VENV_PATH}" ]; then
    source "${VENV_PATH}/bin/activate"
    echo "Activating virtual environment..."
else
    echo "Virtual environment not found at ${VENV_PATH}. Please check the path."
    exit 1
fi
source ${VENV_PATH}/bin/activate

#Execute the python script to update exchange rates
python update_exchange_rates.py
echo "Exchange rates updated at $(date) successfully.">> rate_log.txt