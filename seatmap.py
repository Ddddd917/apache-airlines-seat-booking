
from constants import ROWS, COLUMNS, FREE, RESERVED, AISLE, STORAGE


class SeatMap:
    """
    The SeatMap class handles the structure, initialization, and display
    of the aircraft seating layout. It provides methods to display the seat
    map in a clear format and summarize booking statistics.
    """

    def __init__(self):
        """
        Constructor for SeatMap. Initializes a dictionary-based seat map
        where each key is a seat ID (e.g., '12A') and value is seat status
        ('F' for free, 'R' for reserved, 'S' for storage).
        """
        self.seat_map = self._initialize_seat_map()

    def _initialize_seat_map(self):
        """
        Private method to build the seating layout.
        Rows 77 and 78 columns D, E, F are marked as storage.

        :return: Dictionary representing the full seat layout.
        """
        seat_map = {}
        for row in range(1, ROWS + 1):
            for col in COLUMNS:
                seat_id = f"{row}{col}"
                # Mark last rows DEF as storage
                if row in [77, 78] and col in ['D', 'E', 'F']:
                    seat_map[seat_id] = STORAGE
                else:
                    seat_map[seat_id] = FREE
        return seat_map

    def display_seat_map(self):
        """
        Displays the current seat layout in a formatted view.
        'F' (Free) and 'R' (Reserved) are shown based on real-time seat_map data.
        """
        print("\n----- Seat Layout -----")
        print("     A  B  C|aisle|D  E  F")

        for row in range(1, ROWS + 1):
            row_display = f"{row:<3} "  # Align row numbers to 3 spaces
            for i, col in enumerate(COLUMNS):
                seat_id = f"{row}{col}"
                status = self.seat_map.get(seat_id, '?')  # fallback for missing seat
                seat_display = f" {status} "

                if col == 'C':
                    row_display += seat_display + " |X"
                elif col == 'D':
                    row_display += "| " + seat_display
                else:
                    row_display += seat_display
            print(row_display)

    def display_booking_summary(self):
        """
        Displays a summary of total seats, reserved seats, and available seats.
        Assumes storage seats are not part of total bookable seat count.
        """
        total_seats = 0
        reserved = 0
        free = 0

        for status in self.seat_map.values():
            if status == FREE:
                free += 1
                total_seats += 1
            elif status == RESERVED:
                reserved += 1
                total_seats += 1

        print("\n----- Booking Summary -----")
        print(f"Total Seats Available: {total_seats}")
        print(f"Seats Reserved: {reserved}")
        print(f"Seats Free: {free}")
