# database.py

import sqlite3
from datetime import datetime
from constants import DB_NAME

# 1. Initialize database and create passengers table (if not exists)
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passengers (
            reference_code TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            passport_number TEXT NOT NULL,
            seat_id TEXT NOT NULL,
            timestamp TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

# 2. Insert a new booking record
def insert_booking(reference_code, name, passport_number, seat_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO passengers (reference_code, name, passport_number, seat_id, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (reference_code, name, passport_number, seat_id, timestamp))

    conn.commit()
    conn.close()

# 3. Get booking by reference code
def get_booking_by_reference(reference_code):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM passengers WHERE reference_code = ?
    """, (reference_code,))
    result = cursor.fetchone()

    conn.close()
    return result

# 4. Search booking by name AND passport number
def search_booking(name, passport_number):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM passengers WHERE name = ? AND passport_number = ?
    """, (name, passport_number))
    result = cursor.fetchone()

    conn.close()
    return result

# 5. Delete booking by reference code
def delete_booking(reference_code):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM passengers WHERE reference_code = ?
    """, (reference_code,))
    conn.commit()
    conn.close()