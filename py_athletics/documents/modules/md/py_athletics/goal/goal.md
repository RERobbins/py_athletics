Module py_athletics.goal.goal
=============================
This is the py_athletics goal module.

Classes
-------

`CumulativeGoal(activity_type, metric, target)`
:   CumulativeGoal is a goal measured with respect to all relevant
    Activities without reference to any timeframe.
    
    Create a Goal.
    
    A Goal consists of an activity class, a metric, and a target.
    The metric attribute is a string and the target attribute is an
    integer.
    
    The metric attribute must be one of "count", "distance" or "duration".
    The target attribute must be positive.
    
    There are three Goal subclasses that have different timeframes.
    They are CumulativeGoal, AnnualGoal and MonthGoal.

    ### Ancestors (in MRO)

    * py_athletics.goal.goal.Goal

    ### Methods

    `report(self, athlete) ‑> NoneType`
    :

`Goal(activity_type, metric, target)`
:   py_athletics Goal base class.
    
    Create a Goal.
    
    A Goal consists of an activity class, a metric, and a target.
    The metric attribute is a string and the target attribute is an
    integer.
    
    The metric attribute must be one of "count", "distance" or "duration".
    The target attribute must be positive.
    
    There are three Goal subclasses that have different timeframes.
    They are CumulativeGoal, AnnualGoal and MonthGoal.

    ### Descendants

    * py_athletics.goal.goal.CumulativeGoal
    * py_athletics.goal.goal.MonthGoal
    * py_athletics.goal.goal.YearGoal

    ### Class variables

    `GOAL_METRICS`
    :

    `GOAL_TIMEFRAMES`
    :

    ### Methods

    `report(self, tally: dict) ‑> NoneType`
    :

`MonthGoal(activity_type, metric, target)`
:   MonthGoal is a goal measured with respect to a calendar month.
    
    Create a Goal.
    
    A Goal consists of an activity class, a metric, and a target.
    The metric attribute is a string and the target attribute is an
    integer.
    
    The metric attribute must be one of "count", "distance" or "duration".
    The target attribute must be positive.
    
    There are three Goal subclasses that have different timeframes.
    They are CumulativeGoal, AnnualGoal and MonthGoal.

    ### Ancestors (in MRO)

    * py_athletics.goal.goal.Goal

    ### Methods

    `report(self, athlete) ‑> NoneType`
    :

`YearGoal(activity_type, metric, target)`
:   YearGoal is a goal measured with respect to a calendar year.
    
    Create a Goal.
    
    A Goal consists of an activity class, a metric, and a target.
    The metric attribute is a string and the target attribute is an
    integer.
    
    The metric attribute must be one of "count", "distance" or "duration".
    The target attribute must be positive.
    
    There are three Goal subclasses that have different timeframes.
    They are CumulativeGoal, AnnualGoal and MonthGoal.

    ### Ancestors (in MRO)

    * py_athletics.goal.goal.Goal

    ### Methods

    `report(self, athlete) ‑> NoneType`
    :