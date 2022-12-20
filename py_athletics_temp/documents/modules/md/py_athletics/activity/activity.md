Module py_athletics.activity.activity
=====================================
This is the py_athletics activity module.

Classes
-------

`Activity(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_athletics Activity class.
    
    Create an Activity.
    
    This method requires start and duration arguments and will accept
    keyword arguments for all other attributes.  All Activity subclasses
    call it after they have removed subclass specific keyword arguments.
    Surplus keyword arguments are tolerated and ignored.  Venues are
    currently accepted by not used.

    ### Descendants

    * py_athletics.activity.activity.Cycle
    * py_athletics.activity.activity.Run
    * py_athletics.activity.activity.Tennis
    * py_athletics.activity.activity.Walk
    * py_athletics.activity.activity.Workout

    ### Class variables

    `venue_type_set`
    :

    ### Static methods

    `activity_dictionary() ‑> dict`
    :   Return a dictionary of Activity subclass names to subclasses.

    `subclass_names() ‑> tuple`
    :   Return a tuple of Activity subclass names.

    `subclasses() ‑> tuple`
    :   Return a tuple of Activity subclasses.

    `tally(athlete, class_name: str, start=None, end=None)`
    :   Return a Counter with athlete's aggregated activity data for the specified
        Activity class.  All counters include activity count, calories and
        duration.  Counters for Walk, Cycle and Run include distance.

    ### Instance variables

    `garmin_activity_type: str`
    :   Get the Garmin activity type string used to derive the Activity
        subclass for Activities read from a Garmin activity file.

`Cycle(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_athletics Cycle Activity subclass. A Cycle object may include all
    Activity attributes as well as distance, type, maximum_speed,
    Average_speed, average_power and maximum_average_power attributes.
    Cycle type is a string and can be one of 'commute', 'road', 'trail',or
    'stationary'.  The maximum_speed and average_speed attributes are
    expressed in miles per hour.  The normalized_power attribute is in watts.
    Cycle type is accepted but not yet used.
    
    Create a Cycle Activity. This method requires start and duration
    arguments and will accept keyword arguments for all other Activity and
    Cycle attributes.

    ### Ancestors (in MRO)

    * py_athletics.activity.activity.Activity

    ### Class variables

    `cycle_type_set`
    :

`Run(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_athletics Run Activity subclass.  A Run object may include all
    Activity attributes as well as distance, type, maximum_speed and
    average_speed attributes.  Run type is a string and can be one of
    'track', 'road' or 'treadmill'.  The maximum_speed and average_speed
    attributes are expressed in minutes per mile.  Run type is accepted but
    not yet used.
    
    Create a Run Activity.  This method requires start and duration
    arguments and will accept keyword arguments for all other Activity and
    Run attributes.

    ### Ancestors (in MRO)

    * py_athletics.activity.activity.Activity

    ### Class variables

    `run_type_set`
    :

`Tennis(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_athletics Tennis Activity subclass.  A Tennis object may include all
    Activity attributes as well as type and partner attributes. The type
    attribute is a string and can be one of "ball_machine", "cardio", "drill",
    "hitting_session", "lesson", or "match".  The partner attribute is a
    string.  The type and partner attributes are accepted but not yet used.
    
    Create a Tennis Activity.  This method requires start and duration
    arguments and will accept keyword arguments for all other Activity and
    Tennis attributes.

    ### Ancestors (in MRO)

    * py_athletics.activity.activity.Activity

    ### Class variables

    `tennis_type_set`
    :

`Walk(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_athletics Walk Activity subclass.  A Walk object may include all
    Activity attributes as well as distance, type, maximum_speed and
    average_speed attributes.  Walk type is a string and can be one of
    'track', 'road' or 'treadmill'.  The maximum_speed and average_speed
    attributes are expressed in minutes per mile.  The type attribute is
    accepted but not yet used.
    
    Create a Walk Activity.  This method requires start and duration
    arguments and will accept keyword arguments for all other Activity and
    Walk attributes.

    ### Ancestors (in MRO)

    * py_athletics.activity.activity.Activity

    ### Class variables

    `walk_type_set`
    :

`Workout(start: datetime.datetime, duration: datetime.timedelta, **kwargs)`
:   py_Athletics Workout Activity subclass.  A Workout object may
    include all Activity attributes as well as type and trainer attributes.
    The type attribute is a string and can be either "personal_training" or
    "solo".  The trainer attribute is a string.  The type and trainer
    attributes are accepted but not yet used.
    
    Create a Workout Activity.  This method requires start and duration
    arguments and will accept keyword arguments for all other Activity and
    Workout attributes.

    ### Ancestors (in MRO)

    * py_athletics.activity.activity.Activity

    ### Class variables

    `workout_type_set`
    :