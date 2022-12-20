Module py_athletics.helpers.helpers
===================================
The helpers module provides functions useful to the Activity class methods.
Functions specific to parsing Garmin activity files reside in garmin_helpers.

Functions
---------

    
`is_date(string: str) ‑> bool`
:   Returns True if the string is a valid date of the form YYYY-MM-DD.

    
`none_factory() ‑> NoneType`
:   Return None.

    
`parse_date(string: str) ‑> datetime.date`
:   Parse a string of the form YYYY-MM-DD and return the corresponding
    datetime object.

    
`td_cvt(duration: datetime.timedelta) ‑> tuple`
:   Return number of hours, minutes and seconds represented by a timedelta
    object.