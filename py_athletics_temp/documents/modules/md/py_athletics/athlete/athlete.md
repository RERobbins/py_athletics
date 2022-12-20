Module py_athletics.athlete.athlete
===================================
This is the py_athletics athlete module.

Classes
-------

`Athlete()`
:   py_athletics Athlete class.
    
    Create an Athlete.

    ### Static methods

    `load(filename: str = 'py_athletics.pickle')`
    :   Load Athlete data from a file.
        
        The default filename is py_athletics.pickle, a different name can be
        specified with the filename keyword argument.
        
        Optional Parameters
        -------------------
        filename: string

    ### Methods

    `add_activity(self, activity: activity.activity.Activity) ‑> NoneType`
    :   Add an Activity if the Athlete does not already have an Activity
        of the same type and with the same start datetime.

    `add_goal(self, exercise: str, metric: str, timeframe: str, target: int) ‑> NoneType`
    :   Add a Goal.
        
        A Goal replaces existing Goals for the same activity class and metric.
        The distance metric is only valid for Cycle, Run and Walk activities.
        
        Parameters
        ----------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}
        metric: string = {count|distance|duration}
        timeframe: string = {month|year|cumulative}
        target: a positive integer

    `delete_goal(self, exercise: str, metric: str, timeframe: str) ‑> NoneType`
    :   Delete a Goal.
        
        Parameters
        ----------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}
        metric: string = {count|distance|duration}
        timeframe: string = {month|year|cumulative}

    `earliest_activity(self, exercise: str) ‑> Union[datetime.datetime, NoneType]`
    :   Return a datetime object for the earliest exercise instance.

    `get_activities(self, activity_subclass=None) ‑> list`
    :   Return a list containing an Athlete's activities.  The activities_subclass
        parameter is used to limit the results to the specified subclass.

    `get_goals(self, activity_subclass=None) ‑> list`
    :   Return a list containing an Athlete's goals.  If the optional
        activity_subclass parameter is specified, the result is limited to
        goals for that subclass.

    `read_garmin_activity_file(self, filename='Activities.csv')`
    :   Read a Garmin activity file and create Activity objects.
        
        Garmin fitness data is stored at http://connect.garmin.com.
        Subscribers can download comprehensive activity data into a CSV file.
        This method reads a Garmin activity file, creates py_athletics
        Activity objects and adds them to the Athlete's activity collection.
        
        The  default filename is Activities.csv, a different name can be
        specified with the filename keyword argument.
        
        Optional Parameters
        -------------------
        filename: string

    `save(self, filename: str = 'py_athletics.pickle') ‑> NoneType`
    :   Save Athlete data to a file.
        
        The default filename is py_athletics.pickle, a different name can be
        specified with the filename keyword argument.
        
        Optional Parameters
        -------------------
        filename: string

    `show_activities(self, exercise: str = None, start: str = None, end: str = None) ‑> NoneType`
    :   Display a list of Activities.
        
        If exercise is specified the listing is limited to that exercise.
        A timeframe for the listing can be established with one or both of the
        start and end keywords.
        
        Optional Parameters
        -------------------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}
        start: string in the form YYYY-MM-DD
        end: string in the form YYYY-MM-DD

    `show_goals(self, exercise: str = None) ‑> NoneType`
    :   Display a list of Goals.
        
        If exercise is specified, the listing is limited to that exercise.
        
        Optional Parameters
        -------------------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}

    `summarize_activities(self, exercise=None, start=None, end=None) ‑> NoneType`
    :   Display a summary of Activities.
        
        If exercise is specified the listing is limited to that exercise.
        A timeframe for the listing can be established with one or both of the
        start and end keywords.
        
        Optional Parameters
        -------------------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}
        start: string in the form YYYY-MM-DD
        end: string in the form YYYY-MM-DD

    `summarize_goals(self, exercise=None) ‑> NoneType`
    :   Display a summary of Goals.
        
        If exercise is specified, the listing is limited to that exercise.
        
        Optional Parameters
        -------------------
        exercise: string = {Cycle|Run|Tennis|Walk|Workout}