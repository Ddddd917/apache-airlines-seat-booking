#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:22:30 2025

@author: jaspersdocument
"""

# validation.py

from constants import COLUMNS, ROWS, AISLE, STORAGE

# Check if a seat identifier is valid (e.g., "12A", "80F", etc.)
def is_valid_seat_id(seat_id):
    """
    Validates if the format is correct: number + column letter.
    Does not check whether the seat exists.
    """
    if len(seat_id) < 2 or len(seat_id) > 4:
        return False

    row_part = seat_id[:-1]
    col_part = seat_id[-1].upper()

    if not row_part.isdigit():
        return False

    if col_part not in COLUMNS:
        return False

    return True  # Valid format, but might still be invalid seat number

# Check if the seat exists in the seat map
def seat_exists(seat_id, seat_map):
    """
    Checks whether the seat_id exists in the current seat_map.
    Returns True if found, False if not.
    """
    return seat_id in seat_map

# Check if a seat is bookable (not aisle or storage)
def is_bookable(seat_id, seat_map):
    """
    Returns True if the seat can be booked (i.e., it is not an aisle or storage area).
    """
    status = seat_map.get(seat_id)
    return status not in [AISLE, STORAGE]

# Check if a seat is currently free
def is_seat_free(seat_id, seat_map):
    """
    Returns True if the seat is currently marked as free.
    """
    return seat_map.get(seat_id) == 'F'

# Check if a seat is currently reserved
def is_seat_reserved(seat_id, seat_map):
    """
    Returns True if the seat is currently marked as reserved.
    """
    return seat_map.get(seat_id) == 'R'