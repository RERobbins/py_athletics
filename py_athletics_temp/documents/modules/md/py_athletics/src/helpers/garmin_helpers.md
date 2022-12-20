Module py_athletics.src.helpers.garmin_helpers
==============================================
The garmin_helpers module provides several support functions to ease
handling of the garmin activity file by the Activity class methods.

Functions
---------

    
`garmin_to_decimal(string: str) ‑> Union[NoneType, decimal.Decimal]`
:   Convert a Garmin activity field to a Decimal
    or return None if the field cannot be converted.

    
`garmin_to_int(string: str) ‑> Union[NoneType, int]`
:   Convert a Garmin activity field to an integer
    or return None if the field cannot be converted.

    
`garmin_to_time(string: str) ‑> Union[NoneType, datetime.time]`
:   Convert a Garmin activity field in the form minutes:seconds
    to a datetime.time object or return None if the field cannot be
    converted.