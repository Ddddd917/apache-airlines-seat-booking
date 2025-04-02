
from constants import ROWS, RESERVED


class SeatPreference:
    """
    SeatPreference provides functionality to recommend available seats
    based on user-defined preferences (window, aisle, middle). It searches
    from the front of the plane to the back and suggests up to 4 available seats.
    """

    # Mapping from user preference to seat column letters
    PREFERENCE_MAP = {
        'window': ['A', 'F'],
        'aisle': ['C', 'D'],
        'middle': ['B', 'E']
    }

    def __init__(self, seat_map):
        """
        Initialize with a reference to the seat map dictionary.

        :param seat_map: Dictionary of seat_id -> seat status (F, R, S).
        """
        self.seat_map = seat_map

    def search_by_preference(self):
        """
        Prompts user for seat preference and displays up to 4 available
        seats in preferred columns from the front of the aircraft.
        """
        print("\n--- Seat Preference Search ---")
        print("Please enter your seat preference: window, aisle, or middle")
        preference = input("Your preference: ").strip().lower()

        if preference not in self.PREFERENCE_MAP:
            print("❌ Invalid preference. Please enter 'window', 'aisle', or 'middle'.\n")
            return

        preferred_columns = self.PREFERENCE_MAP[preference]
        matching_seats = []

        # Inform the user that the system will prioritize front-row seats
        print("System will recommend front-row available seats by default...\n")

        # Search from row 1 to ROWS for matching free seats
        for row in range(1, ROWS + 1):
            for col in preferred_columns:
                seat_id = f"{row}{col}"
                if seat_id in self.seat_map and self.seat_map[seat_id] != RESERVED:
                    matching_seats.append(seat_id)
                    if len(matching_seats) == 4:
                        break
            if len(matching_seats) == 4:
                break

        # Output matching seat suggestions
        if matching_seats:
            print("Recommended seats based on your preference:")
            print(" -> " + ", ".join(matching_seats))
        else:
            print("Sorry, no seats available that match your preference.")
