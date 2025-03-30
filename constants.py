#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 21:14:32 2025

@author: jaspersdocument
"""

# constants.py

# Seat status symbols
FREE = 'F'
RESERVED = 'R'
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