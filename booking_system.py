from seatmap import SeatMap
from booking import BookingManager
from validation import Validator
from database import DatabaseManager
from preference import SeatPreference
from search import SearchManager
from constants import RESERVED, FREE,REFERENCE_CODE_LENGTH

class BookingSystem:
    """
    BookingSystem controls the overall airline seat booking process.
    It integrates all modular components into a cohesive command-line system.
    """

    def __init__(self):
        """
        Initializes the booking system:
        - Sets up the database
        - Instantiates all module managers
        - Prepares the in-memory seat map
        """
        self.db = DatabaseManager()
        self.seat_map_obj = SeatMap()
        self.seat_map = self.seat_map_obj.seat_map  # Pass to others
        self.booking_manager = BookingManager(self.seat_map)
        self.preference_manager = SeatPreference(self.seat_map)
        self.search_manager = SearchManager(self.db)

    def show_menu(self):
        """
        Displays the main command-line menu options to the user.
        """
        print("\n===== Apache Airlines Seat Booking System =====")
        print("1. Check Seat Availability")
        print("2. Book a Seat")
        print("3. Cancel Booking by Reference Code")
        print("4. Show Seats Layout and Booking Status")
        print("5. Group Booking")
        print("6. Seat Preference Search")
        print("7. Search Booking by Identity")
        print("8. Exit Program")
        print("\n💡 If you've forgotten your booking reference, use option 7 to retrieve it.")

    def check_availability(self):
        """
        Allows the user to input a seat ID and check whether it is
        available, reserved, or does not exist.
        """
        seat_id = input("Enter the seat to check (e.g., 15B): ").strip().upper()

        if not Validator.is_valid_seat_id(seat_id):
            print("❌ Invalid seat format. Please enter a seat like '15B'.")
            return

        if not Validator.seat_exists(seat_id, self.seat_map):
            print("❌ That seat does not exist.")
            return

        if Validator.is_seat_free(seat_id, self.seat_map):
            print(f"✅ Seat {seat_id} is available.")
        elif Validator.is_seat_reserved(seat_id, self.seat_map):
            print(f"❌ Seat {seat_id} is already reserved.")
        else:
            print(f"⚠️ Seat {seat_id} cannot be booked.")

    def run(self):
        """
        Runs the main loop of the program, listening for user choices
        and delegating actions to the appropriate module or function.
        """
        while True:
            self.show_menu()
            choice = input("Select an option (1-8): ").strip()

            if choice == '1':
                self.check_availability()
            elif choice == '2':
                self.booking_manager.book_seat()
            elif choice == '3':
                self.booking_manager.cancel_by_reference()
            elif choice == '4':
                self.seat_map_obj.display_seat_map()
                self.seat_map_obj.display_booking_summary()
            elif choice == '5':
                self.booking_manager.group_booking()
            elif choice == '6':
                self.preference_manager.search_by_preference()
            elif choice == '7':
                self.search_manager.search_booking_by_identity()
            elif choice == '8':
                print("Thank you for using Apache Airlines Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.\n")

if __name__ == "__main__":
    system = BookingSystem()
    system.run()