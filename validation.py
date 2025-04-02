
import re
from constants import COLUMNS, ROWS, STORAGE, RESERVED, FREE, REFERENCE_CODE_LENGTH


class Validator:
    """
    Validator is a static utility class that provides input validation
    methods for seat IDs, passport numbers, reference codes, and seat status.
    All methods are static and can be called without class instantiation.
    """

    @staticmethod
    def is_valid_seat_id(seat_id):
        """
        Checks if a seat identifier (e.g., "12A") is in valid format.
        Does not check if the seat actually exists.

        :param seat_id: String seat identifier.
        :return: True if format is correct, False otherwise.
        """
        if len(seat_id) < 2 or len(seat_id) > 4:
            return False

        row_part = seat_id[:-1]
        col_part = seat_id[-1].upper()

        if not row_part.isdigit():
            return False
        if col_part not in COLUMNS:
            return False

        return True

    @staticmethod
    def seat_exists(seat_id, seat_map):
        """
        Checks whether a given seat_id exists in the provided seat map.

        :param seat_id: String like "12A".
        :param seat_map: Dictionary of all seat IDs and their status.
        :return: True if seat exists in seat_map.
        """
        return seat_id in seat_map

    @staticmethod
    def is_bookable(seat_id, seat_map):
        """
        Checks if a seat is bookable (not a storage seat).

        :param seat_id: Seat identifier.
        :param seat_map: Dictionary of all seat IDs.
        :return: True if seat is not a storage seat.
        """
        return seat_map.get(seat_id) != STORAGE

    @staticmethod
    def is_seat_free(seat_id, seat_map):
        """
        Checks if a seat is currently free.

        :param seat_id: Seat identifier.
        :param seat_map: Dictionary of all seat IDs.
        :return: True if the seat is free.
        """
        return seat_map.get(seat_id) == FREE

    @staticmethod
    def is_seat_reserved(seat_id, seat_map):
        """
        Checks if a seat is currently reserved.

        :param seat_id: Seat identifier.
        :param seat_map: Dictionary of all seat IDs.
        :return: True if the seat is reserved.
        """
        return seat_map.get(seat_id) == RESERVED

    @staticmethod
    def is_valid_passport_number(passport_number):
        """
        Validates the format of a passport number (alphanumeric, 6–9 characters).

        :param passport_number: String input by user.
        :return: True if format is acceptable.
        """
        return bool(re.fullmatch(r'[A-Za-z0-9]{6,9}', passport_number))

    @staticmethod
    def is_valid_reference_code(ref_code):
        """
        Validates the reference code format (length and alphanumeric).

        :param ref_code: String input by user.
        :return: True if reference code matches expected format.
        """
        return len(ref_code) == REFERENCE_CODE_LENGTH and ref_code.isalnum()
