
from validation import Validator


class SearchManager:
    """
    This class handles the logic for searching a booking by passenger identity.
    It queries the database using a provided DatabaseManager instance.
    """

    def __init__(self, database_manager):
        """
        Initializes SearchManager with a reference to a database manager.

        :param database_manager: An instance of DatabaseManager for DB access.
        """
        self.db = database_manager

    def search_booking_by_identity(self):
        """
        Prompts user to input full name and passport number.
        If a matching record is found in the database, displays the reference code,
        seat number, and booking timestamp. Otherwise, informs the user.
        """
        print("\n--- Search Booking ---")
        name = input("Enter Full Name: ").strip()
        passport = input("Enter Passport Number: ").strip()

        if not Validator.is_valid_passport_number(passport):
            print("❌ Invalid passport number format.\n")
            return

        result = self.db.search_booking_by_identity(name, passport)

        if result:
            reference = result['reference_code']
            seat_id = result['seat']
            print("\n✅ Booking found!")
            print(f"Reference Code: {reference}")
            print(f"Seat: {seat_id}\n")
        else:
            print("❌ No booking found with the provided name and passport number.\n")
