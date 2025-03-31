#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:26:39 2025

@author: jaspersdocument
"""

# main.py

from seatmap import initialize_seat_map, display_seat_map
from booking import book_seat, cancel_by_reference
from validation import is_valid_seat_id, seat_exists, is_bookable, is_seat_free, is_seat_reserved
from booking import group_booking
from preference import seat_preference_search
from database import init_db
from search import search_booking_by_identity

def check_availability(seat_map):
    """
    Allows the user to input a seat ID and check whether it is available, reserved,
    or unbookable (aisle or storage).
    """
    seat_id = input("Enter the seat to check (e.g., 15B): ").strip().upper()

    if not is_valid_seat_id(seat_id):
        print()
        print("Invalid seat format. Please enter a seat like '15B'.")
        return

    if not seat_exists(seat_id, seat_map):
        print()
        print("That seat does not exist.")
        return

    if not is_bookable(seat_id, seat_map):
        print()
        print(f"Seat {seat_id} is not bookable (aisle or storage area).")
        return

    if is_seat_free(seat_id, seat_map):
        print()
        print(f"Seat {seat_id} is available.")
    elif is_seat_reserved(seat_id, seat_map):
        print()
        print(f"Seat {seat_id} is already reserved.")
    else:
        print()
        print(f"Seat {seat_id} has an unknown status.")
def show_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n===== Apache Airlines Seat Booking System =====")
    print("1. Check Seat Availability")
    print("2. Book a Seat")
    print("3. Cancel Booking by Reference Code")
    print("4. Show Seat Layout and Booking Summary")
    print("5. Group Booking")
    print("6. Seat Preference Search")
    print("7. Search Booking by Name and Passport Number")
    print("8. Exit Program")

    print("\n💡 If you forgot your reference code, you can retrieve it using option 7.")

def main():
    """
    Main control loop for the booking system.
    """
    init_db()  # Ensure database and table exist
    seat_map = initialize_seat_map()

    while True:
        show_menu()
        choice = input("Select an option (1-8): ").strip()

        if choice == '1':
            check_availability(seat_map)
        elif choice == '2':
            book_seat(seat_map)
        elif choice == '3':
            cancel_by_reference(seat_map)
        elif choice == '4':
            display_seat_map(seat_map)
        elif choice == '5':
            group_booking(seat_map)
        elif choice == '6':
            seat_preference_search(seat_map)
        elif choice == '7':
            search_booking_by_identity()
        elif choice == '8':
            print("Thank you for using Apache Airlines Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.\n")
if __name__ == "__main__":
    main()

