"""The garmin_helpers module provides several support functions to ease
handling of the garmin activity file by the Activity class methods."""

from decimal import Decimal
from datetime import datetime, time
from typing import Union


def garmin_to_int(string: str) -> Union[None, int]:
    """Convert a Garmin activity field to an integer
    or return None if the field cannot be converted."""

    # Garmin uses "--" or "0" to indicate None.
    # Garmin integer strings can include commas, we remove those
    # before attempting to cast the string to an int.

    if not string or string == "--" or string == "0":
        return None
    if "," in string:
        string = string.replace(",", "")
    return int(string)


def garmin_to_decimal(string: str) -> Union[None, Decimal]:
    """Convert a Garmin activity field to a Decimal
    or return None if the field cannot be converted."""

    # Garmin uses "--" or "0" to indicate None.
    # Garmin number strings can include commas, we remove those
    # before attempting to cast the string to a Decimal.

    if not string or string == "--" or string == "0":
        return None
    if "," in string:
        string = string.replace(",", "")
    return Decimal(string)


def garmin_to_time(string: str) -> Union[None, time]:
    """Convert a Garmin activity field in the form minutes:seconds
    to a datetime.time object or return None if the field cannot be
    converted."""

    # Garmin uses "--" or "0" to indicate None.

    if not string or string == "--" or string == "0":
        return None
    return datetime.time(datetime.strptime(string, "%M:%S"))
