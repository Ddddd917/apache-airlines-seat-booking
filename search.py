# search.py

from database import search_booking
from validation import is_valid_passport_number

def search_booking_by_identity():
    """
    Allows the user to retrieve their booking using full name and passport number.
    If a matching booking is found, the system will display the reference code.
    """
    print("\n--- Search Booking ---")
    name = input("Enter Full Name: ").strip()
    passport = input("Enter Passport Number: ").strip()

    if not is_valid_passport_number(passport):
        print("❌ Invalid passport number format.\n")
        return

    result = search_booking(name, passport)

    if result:
        reference, _, _, seat_id, timestamp = result
        print("\n✅ Booking found!")
        print(f"Reference Code: {reference}")
        print(f"Seat: {seat_id}")
        print(f"Booked at: {timestamp}\n")
    else:
        print("❌ No booking found with the provided name and passport number.\n")