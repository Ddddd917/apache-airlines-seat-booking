#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:25:16 2025

@author: jaspersdocument
"""

# booking.py
import random
import string
from constants import RESERVED, FREE
from validation import (
    is_valid_seat_id,
    seat_exists,
    is_bookable,
    is_seat_free,
    is_seat_reserved
)
from database import insert_booking, get_booking_by_reference, delete_booking

def generate_reference_code():
    """
    Generates an 8-character alphanumeric reference code.
    Ensures it's unique by checking the database.
    """
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not get_booking_by_reference(code):  # Make sure it doesn't exist
            return code

# Function to book a single seat
def book_seat(seat_map):
    """
    Books a single seat: validates input, collects passenger info,
    generates reference, saves to DB, and confirms booking.
    """
    while True:
        seat_id = input("Enter the seat you want to book (e.g., 12A): ").strip().upper()

        if not is_valid_seat_id(seat_id):
            print("Invalid seat format. Please enter a seat like '12A'.\n")
            continue

        if not seat_exists(seat_id, seat_map):
            print("That seat does not exist. Valid seats are from 1A to 80F.\n")
            continue

        if not is_bookable(seat_id, seat_map):
            print("This seat cannot be booked. It may be an aisle or storage area.\n")
            return

        if not is_seat_free(seat_id, seat_map):
            print(f"Seat {seat_id} is already reserved.\n")
            return

        # Step 1: Reserve seat in seat_map
        seat_map[seat_id] = RESERVED

        # Step 2: Collect passenger info
        print("\n✅ Seat is available. Please enter passenger details.")
        name = input("Full Name: ").strip()
        passport_number = input("Passport Number: ").strip()

        # Step 3: Generate unique booking reference
        reference_code = generate_reference_code()

        # Step 4: Insert booking into the database
        insert_booking(reference_code, name, passport_number, seat_id)

        # Step 5: Confirm booking
        print(f"\n✅ Seat {seat_id} has been successfully booked!")
        print(f"🔖 Your booking reference code is: {reference_code}")
        print("⚠️  Please save this code to manage your booking later.\n")
        return

def cancel_by_reference(seat_map):
    """
    Cancels a booking using the booking reference code.
    If the booking exists, it removes it from the database and frees the seat.
    """
    print("\n--- Cancel Booking ---")
    ref = input("Enter your 8-character booking reference code: ").strip().upper()

    booking = get_booking_by_reference(ref)
    if not booking:
        print("❌ Booking not found. Please check your reference code.\n")
        return

    _, name, passport, seat_id, _ = booking

    # Step 1: Free the seat in seat_map
    if seat_id in seat_map:
        seat_map[seat_id] = 'F'

    # Step 2: Delete from database
    delete_booking(ref)

    # Step 3: Confirm cancellation
    print(f"\n✅ Booking cancelled successfully!")
    print(f"Passenger: {name}")
    print(f"Seat {seat_id} is now available again.")
    print("Reference code:", ref)
    print()

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
    Allows group booking of up to 3 seats.
    For each seat, prompts the user to input passenger info,
    generates a unique reference, and saves the record to the database.
    """
    print("\n--- Group Booking ---")
    print("You can book up to 3 seats that are adjacent.")
    input_line = input("Enter up to 3 seat IDs (e.g., 12A 12B 12C): ").strip().upper()

    seat_list = input_line.split()

    if not (1 <= len(seat_list) <= 3):
        print("❌ Please enter between 1 and 3 seats.\n")
        return

    invalid_seats = []
    for seat_id in seat_list:
        if not is_valid_seat_id(seat_id):
            invalid_seats.append(f"{seat_id} (invalid format)")
        elif not seat_exists(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (does not exist)")
        elif not is_bookable(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (not bookable)")
        elif not is_seat_free(seat_id, seat_map):
            invalid_seats.append(f"{seat_id} (already reserved)")

    if invalid_seats:
        print("\n❌ Group booking failed due to the following issues:")
        for issue in invalid_seats:
            print(" -", issue)
        print("No seats were booked.\n")
        return

    references = []

    # All seats are valid → proceed
    for seat_id in seat_list:
        print(f"\n🔹 Passenger details for seat {seat_id}:")
        name = input("Full Name: ").strip()
        passport_number = input("Passport Number: ").strip()

        # Mark seat as reserved
        seat_map[seat_id] = RESERVED

        # Generate unique reference
        reference_code = generate_reference_code()
        insert_booking(reference_code, name, passport_number, seat_id)
        references.append((seat_id, reference_code))

    # Show final confirmation
    print("\n✅ Group booking successful!")
    for seat_id, ref in references:
        print(f"Seat {seat_id} → Reference: {ref}")
    print("⚠️  Please save these reference codes to manage your bookings later.\n")


# 生成 reference code 的函数（若未定义则添加）
def generate_reference_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if not get_booking_by_reference(code):
            return code

"""
def group_booking(seat_map):

    Allows the user to book multiple seats at once.
    If any seat is invalid, already booked, or unbookable, the entire operation is cancelled.
    
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
"""