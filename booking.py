#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:25:16 2025

@author: jaspersdocument
"""

# booking.py

from constants import RESERVED, FREE
from validation import (
    is_valid_seat_id,
    seat_exists,
    is_bookable,
    is_seat_free,
    is_seat_reserved
)

# Function to book a single seat
def book_seat(seat_map):
    """
    Prompts the user to enter a seat ID and attempts to reserve the seat.
    It validates the seat format, checks if the seat exists and is bookable,
    and then reserves it if it's currently free.
    """
    seat_id = input("Enter the seat you want to book (e.g., 12A): ").strip().upper()

    if not is_valid_seat_id(seat_id):
        print()
        print("Invalid seat format. Please enter a seat like '12A'.")
        return

    if not seat_exists(seat_id, seat_map):
        print()
        print("That seat does not exist.")
        return

    if not is_bookable(seat_id, seat_map):
        print()
        print("This seat cannot be booked. It may be an aisle or storage area.")
        return

    if not is_seat_free(seat_id, seat_map):
        print()
        print(f"Seat {seat_id} is already reserved.")
        return

    seat_map[seat_id] = RESERVED
    print()
    print(f"Seat {seat_id} has been successfully booked.")

# Function to cancel (free) a reserved seat
def cancel_seat(seat_map):
    """
    Prompts the user to enter a seat ID and attempts to cancel the reservation.
    Only seats that are currently reserved can be freed.
    """
    seat_id = input("Enter the seat you want to cancel (e.g., 12A): ").strip().upper()

    if not is_valid_seat_id(seat_id):
        print()
        print("Invalid seat format. Please enter a seat like '12A'.")
        return

    if not seat_exists(seat_id, seat_map):
        print()
        print("That seat does not exist.")
        return

    if not is_bookable(seat_id, seat_map):
        print()
        print("This seat is not a reservable seat.")
        return

    if not is_seat_reserved(seat_id, seat_map):
        print()
        print(f"Seat {seat_id} is not currently reserved.")
        return

    seat_map[seat_id] = FREE
    print()
    print(f"Seat {seat_id} has been successfully canceled and is now available.")

def group_booking(seat_map):
    """
    Allows the user to book multiple seats at once.
    If any seat is invalid, already booked, or unbookable, the entire operation is cancelled.
    """
    print("\n--- Group Booking ---")
    print("Enter multiple seat IDs separated by spaces (e.g., 12A 12B 12C):")
    input_line = input("Seats to book: ").strip().upper()

    seat_list = input_line.split()
    invalid_seats = []

    # Step 1: Validate all seats first
    for seat_id in seat_list:
        if not is_valid_seat_id(seat_id):
            invalid_seats.append(f"{seat_id} (invalid format)")
        elif not seat_exists(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (does not exist)")
        elif not is_bookable(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (not bookable)")
        elif not is_seat_free(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (already reserved)")

    # Step 2: If any errors, cancel entire booking
    if invalid_seats:
        print("\n❌ Group booking failed due to the following issues:")
        for error in invalid_seats:
            print(" -", error)
        print("No seats were booked.\n")
        return

    # Step 3: All seats valid and free → proceed with booking
    for seat_id in seat_list:
        seat_map[seat_id] = RESERVED

    print("\n✅ Group booking successful!")
    print("Seats booked:", ' '.join(seat_list), "\n")