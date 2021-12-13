import json
from numpy import NaN
import pandas as pd

garmin_directory = "/home/rerobbins/garmin_data/DI_CONNECT/DI-Connect-Fitness"
json_file_0 = garmin_directory + "/rerobbins_0_summarizedActivities.json"
json_file_1 = garmin_directory + "/rerobbins_1001_summarizedActivities.json"

with open(json_file_0) as f:
    data_0 = json.load(f)

with open(json_file_1) as f:
    data_1 = json.load(f)

df_0 = pd.json_normalize(data_0, record_path="summarizedActivitiesExport")
df_1 = pd.json_normalize(data_1, record_path="summarizedActivitiesExport")

df = pd.concat([df_0, df_1], join="outer", ignore_index=True)
df = df.set_index(pd.to_datetime(df["startTimeLocal"], unit="ms"))

# We will derive avgPaceMPM later, but create a spot for it here.

df['avgPaceMPM'] = NaN

available_columns = df.columns

of_interest = [
    "activityId",
    "name",
    "activityType",
    "sportType",
    "duration",
    "elapsedDuration",
    "movingDuration",
    "avgHr",
    "maxHr",
    "calories",
    "bmrCalories",
    "distance",
    "avgSpeed",
    "maxSpeed",
    "avgPaceMPM",
    "maxRunCadence",
    "avgBikeCadence",
    "maxBikeCadence",
    "avgPower",   
    "normPower",
    "steps",
    "trainingEffectLabel",
    "activityTrainingLoad",
    "aerobicTrainingEffectMessage",
    "anaerobicTrainingEffectMessage",
    "moderateIntensityMinutes",
    "vigorousIntensityMinutes",
]

df = df[of_interest]

df.duration = pd.to_timedelta(df.duration, unit="ms")
df.elapsedDuration = pd.to_timedelta(df.elapsedDuration, unit="ms")
df.movingDuration = pd.to_timedelta(df.movingDuration, unit="ms")
df.avgHr = df.avgHr.round(0).astype("Int16")
df.maxHr = df.maxHr.round(0).astype("Int16")
df.calories = df.calories.round(0).astype("Int16")
df.bmrCalories = df.bmrCalories.round(0).astype("Int16")

# Distance seems to be recorded in centimeters.
# One mile has 160934.4 centimeters

df.distance = df.distance / 160934.3
df.rename(columns={"distance": "distanceMiles"}, inplace=True)

# Speed (at least for cycling) seems to be recorded in dekameters per second.
# One dekameter per second is 22.369363 miles per hour.

df.avgSpeed = df.avgSpeed * 22.369363
df.maxSpeed = df.maxSpeed * 22.369363
df.rename(columns={"avgSpeed": "avgSpeedMPH", "maxSpeed": "maxSpeedMPH"},
          inplace=True)

# Pace in minutes per mile is 60/MPH, only set it where avgSpeedMPH > 0

mask = df.avgSpeedMPH > 0
df.loc[mask, 'avgPaceMPM'] = 60 / df.avgSpeedMPH
