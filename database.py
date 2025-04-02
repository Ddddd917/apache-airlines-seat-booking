
import sqlite3
from datetime import datetime
from constants import DB_NAME


class DatabaseManager:
    """
    This class handles all database operations related to the Apache Airlines
    seat booking system. It manages creating the table, inserting bookings,
    retrieving booking information, deleting records, and searching bookings
    by passenger identity.
    """

    def __init__(self, db_name=DB_NAME):
        """
        Initializes the DatabaseManager with the database file name.
        Automatically calls init_db to ensure the table exists.

        :param db_name: The name/path of the SQLite database file.
        """
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """
        Initializes the SQLite database and creates the passengers table if it doesn't already exist.
        The table includes reference_code, name, passport_number, seat_id, and timestamp.
        """
        conn = sqlite3.connect(self.db_name)
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

    def insert_booking(self, reference_code, name, passport_number, seat_id):
        """
        Inserts a new booking record into the passengers table.

        :param reference_code: The unique reference code for the booking.
        :param name: Full name of the passenger.
        :param passport_number: Passport number of the passenger.
        :param seat_id: Seat identifier (e.g., "12A").
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Record timestamp of booking
        cursor.execute("""
            INSERT INTO passengers (reference_code, name, passport_number, seat_id, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (reference_code, name, passport_number, seat_id, timestamp))
        conn.commit()
        conn.close()

    def get_booking_by_reference(self, reference_code):
        """
        Retrieves a booking record using the reference code.

        :param reference_code: The unique booking code.
        :return: Dictionary with name, passport number, and seat if found; else None.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name, passport_number, seat_id FROM passengers WHERE reference_code = ?
        """, (reference_code,))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {
                "name": result[0],
                "passport_number": result[1],
                "seat": result[2]
            }
        return None

    def delete_booking(self, reference_code):
        """
        Deletes a booking from the database using its reference code.

        :param reference_code: The unique reference code to identify the booking.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM passengers WHERE reference_code = ?", (reference_code,))
        conn.commit()
        conn.close()

    def search_booking_by_identity(self, name, passport_number):
        """
        Searches the database for a booking using a passenger's full name and passport number.

        :param name: Full name of the passenger.
        :param passport_number: Passport number of the passenger.
        :return: Dictionary with reference_code and seat if found; else None.
        """
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT reference_code, seat_id FROM passengers
            WHERE name = ? AND passport_number = ?
        """, (name, passport_number))
        result = cursor.fetchone()
        conn.close()
        if result:
            return {
                "reference_code": result[0],
                "seat": result[1]
            }
        return None
