#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:17:08 2025

@author: jaspersdocument
"""

# seatmap.py

from constants import ROWS, COLUMNS, FREE, RESERVED, AISLE, STORAGE

# Function to initialize the seat map with default values
def initialize_seat_map():
    seat_map = {}
    for row in range(1, ROWS + 1):
        for col in COLUMNS:
            seat_id = f"{row}{col}"
            # For rows 77 to 80, columns D, E, F are storage areas
            if row in [77, 78] and col in ['D', 'E', 'F']:
                seat_map[seat_id] = STORAGE
            else:
                seat_map[seat_id] = FREE  # All other seats are initially free
    return seat_map

# Function to print the seat map in a clear and aligned format
def display_seat_map(seat_map):
    print("\n------------ Seat Layout --------")
    print()
    # Print the top header row showing seat columns and aisle
    print("     A   B   C  aisle D   E   F")
    print()
    # Iterate through all 80 rows of the aircraft
    for row in range(1, ROWS + 1):
        # Start the line with the row number, left-aligned, padded to 2 characters
        row_str = f"{row:<2}  "

        # Print seats on the left side of the aisle (columns A, B, C)
        for col in ['A', 'B', 'C']:
            seat_id = f"{row}{col}"
            status = seat_map.get(seat_id, ' ')
            if status == RESERVED:
                row_str += "<R> "  # Highlight reserved seats
            elif status == FREE:
                row_str += " F  "  # Free seats
            elif status == STORAGE:
                row_str += " S  "  # Storage area
            else:
                row_str += f" {status}  "  # Fallback

        # Insert visual representation of aisle in the middle
        row_str += "｜X｜ "

        # Print seats on the right side of the aisle (columns D, E, F)
        for col in ['D', 'E', 'F']:
            seat_id = f"{row}{col}"
            status = seat_map.get(seat_id, ' ')
            if status == RESERVED:
                row_str += "<R> "  # Highlight reserved seats
            elif status == FREE:
                row_str += " F  "  # Free seats
            elif status == STORAGE:
                row_str += " S  "  # Storage area
            else:
                row_str += f" {status}  "  # Fallback

        # Print the formatted row string
        print(row_str)

    # Print the legend to explain seat symbols
    print("\nLegend: <R> = Reserved, F = Free, ｜X｜ = Aisle, S = Storage")