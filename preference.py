# preference.py

from constants import ROWS, RESERVED

# Mapping from preference keyword to columns
PREFERENCE_MAP = {
    'window': ['A', 'F'],
    'aisle': ['C', 'D'],
    'middle': ['B', 'E']
}

def seat_preference_search(seat_map):
    """
    Allows the user to input a seat type preference (window/aisle/middle)
    and recommends up to 4 available seats near the front.
    """
    print("\n--- Seat Preference Search ---")
    print("Please enter your seat preference: window, aisle, or middle")
    preference = input("Your preference: ").strip().lower()

    if preference not in PREFERENCE_MAP:
        print("Invalid preference. Please enter 'window', 'aisle', or 'middle'.\n")
        return

    preferred_columns = PREFERENCE_MAP[preference]
    matching_seats = []

    # Search from row 1 to 80 for matching free seats
    for row in range(1, ROWS + 1):
        for col in preferred_columns:
            seat_id = f"{row}{col}"
            if seat_id in seat_map and seat_map[seat_id] != RESERVED:
                matching_seats.append(seat_id)
                if len(matching_seats) >= 4:
                    break
        if len(matching_seats) >= 4:
            break

    print(f"\n🪑 Available {preference.title()} Seats Recommendation:")
    if matching_seats:
        print("Recommended seats:", ' '.join(matching_seats))
    else:
        print("Sorry, no available seats match your preference.")
    print()