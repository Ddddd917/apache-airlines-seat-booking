#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:14:32 2025

@author: jaspersdocument
"""

# constants.py

# Reference code settings
REFERENCE_CODE_LENGTH = 8

# Database file name
DB_NAME = "flight757_booking.db"

# Seat status symbols
FREE = 'F'
RESERVED = '<R>'
AISLE = 'X'
STORAGE = 'S'

# Seat layout configuration
ROWS = 80
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F']

# Columns that are non-bookable (optional by layout design)
NON_BOOKABLE_POSITIONS = {
    'X': AISLE,
    'S': STORAGE
}