#  Database connection

import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DATABASE_PASSWORD"),

        database="gift_db"
    )