import random
import string
from constants import RESERVED, FREE, REFERENCE_CODE_LENGTH
from validation import Validator
from database import DatabaseManager


class BookingManager:
    """
    The BookingManager class encapsulates all operations related to seat booking,
    including single seat booking, group booking, and cancellation using a
    booking reference code. It interacts with both the in-memory seat map and
    the database to maintain consistency.
    """

    def __init__(self, seat_map):
        """
        Initializes the BookingManager with a reference to the current seat map.

        :param seat_map: A 2D list representing the seating layout and current seat states.
        """
        self.seat_map = seat_map
        self.db = DatabaseManager()

    def generate_reference_code(self):
        """
        Generates a unique 8-character alphanumeric booking reference code.
        The code is checked against the database to ensure uniqueness.

        :return: A unique booking reference string.
        """
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=REFERENCE_CODE_LENGTH))
            if not self.db.get_booking_by_reference(code):  # Ensure reference code is not already used
                return code

    def book_seat(self):
        """
        Handles the process of booking a single seat.
        The method includes input validation, passenger detail collection,
        reference code generation, database insertion, and seat map update.
        """
        while True:
            seat_id = input("Enter the seat you want to book (e.g., 12A): ").strip().upper()

            if not Validator.is_valid_seat_id(seat_id):
                print("Invalid seat format. Please enter a seat like '12A'.")
                continue

            if not Validator.seat_exists(seat_id, self.seat_map):
                print("That seat does not exist. Valid seats range from 1A to 80F.")
                continue

            if not Validator.is_seat_free(seat_id, self.seat_map):
                print(f"Seat {seat_id} is already booked.")
                return

            name = input("Enter passenger full name: ").strip()
            passport = input("Enter passport number: ").strip()

            reference = self.generate_reference_code()

            self.db.insert_booking(reference, name, passport, seat_id)

            # Mark the seat as reserved in the in-memory seat map
            self.seat_map[seat_id] = RESERVED

            print(f"✅ Seat {seat_id} has been successfully booked.")
            print(f"🧾 Booking reference: {reference}")
            return

    def cancel_by_reference(self):
        """
        Cancels an existing seat booking using a reference code.
        If the reference is valid and found in the database,
        the associated seat is released and database record removed.
        """
        ref = input("Enter your 8-character booking reference code: ").strip().upper()
        booking = self.db.get_booking_by_reference(ref)

        if not booking:
            print("❌ Booking reference not found.")
            return

        seat_id = booking['seat']
        self.db.delete_booking(ref)

        # Mark the seat as free in the in-memory seat map
        self.seat_map[seat_id] = FREE

        print(f"✅ Booking for seat {seat_id} has been successfully cancelled.")

    def group_booking(self):
        """
        Allows a passenger to book up to three adjacent seats in a single transaction.
        For each seat, user is prompted to input passenger details.
        All bookings are inserted into the database, and seats are marked as reserved.
        """
        print("You can book up to 3 adjacent seats.")
        seat_ids = input("Enter up to 3 adjacent seat IDs separated by space (e.g., 12A 12B 12C): ").strip().upper().split()

        if len(seat_ids) == 0 or len(seat_ids) > 3:
            print("❌ Please enter between 1 to 3 seat IDs.")
            return

        # Validate all seats before proceeding
        for seat_id in seat_ids:
            if not Validator.is_valid_seat_id(seat_id) or not Validator.seat_exists(seat_id, self.seat_map):
                print(f"❌ Seat {seat_id} is invalid or does not exist.")
                return
            if not Validator.is_seat_free(seat_id, self.seat_map):
                print(f"❌ Seat {seat_id} is already booked.")
                return

        # Collect passenger details and book each seat
        for seat_id in seat_ids:
            print(f"Entering passenger details for seat {seat_id}:")
            name = input("Enter full name: ").strip()
            passport = input("Enter passport number: ").strip()
            if not Validator.is_valid_passport_number(passport):
                print("❌ Invalid passport number format. Must be 6–9 alphanumeric characters.\\n")
                return
            reference = self.generate_reference_code()

            self.db.insert_booking(reference, name, passport, seat_id)
            self.seat_map[seat_id] = RESERVED

            print(f"✅ Seat {seat_id} booked successfully.")
            print(f"🧾 Booking reference: {reference}")
