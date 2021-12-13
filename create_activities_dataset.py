import json
import pandas as pd

json_directory = "/home/rerobbins/garmin_data/DI_CONNECT/DI-Connect-Fitness"
json_file_0 = json_directory + "/rerobbins_0_summarizedActivities.json"
json_file_1 = json_directory + "/rerobbins_1001_summarizedActivities.json"

with open(json_file_0) as f:
    data_0 = json.load(f)

with open(json_file_1) as f:
    data_1 = json.load(f)

raw_df_0 = pd.json_normalize(data_0, record_path="summarizedActivitiesExport")
raw_df_1 = pd.json_normalize(data_1, record_path="summarizedActivitiesExport")

raw_df = pd.concat([raw_df_0, raw_df_1], join="outer", ignore_index=True)

# Derive timestamp objects to use as index.

raw_df = raw_df.set_index(pd.to_datetime(raw_df["startTimeLocal"], unit="ms"))

# Filter columns to retain.

mask = [
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
    "distance",
    "avgSpeed",
    "maxSpeed",
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

df = raw_df[mask].copy()

# Filter columns to round to 0 and convert to nullable integers with NA for 0.

mask = [
    "movingDuration",
    "avgHr",
    "maxHr",
    "calories",
    "maxRunCadence",
    "avgBikeCadence",
    "maxBikeCadence",
    "avgPower",
    "normPower",
    "steps",
]

df[mask] = df[mask].round(0).convert_dtypes().replace(0, pd.NA)

# Derive duration fields.

df.duration = pd.to_timedelta(df.duration, unit="ms")
df.elapsedDuration = pd.to_timedelta(df.elapsedDuration, unit="ms")
df.movingDuration = pd.to_timedelta(df.movingDuration, unit="ms")

# Distance in centimeters, one mile has 160934.4 centimeters.

df.distance = df.distance / 160934.3
df.rename(columns={"distance": "distanceMiles"}, inplace=True)

# Speed is recorded in dekameters per second.
# One dekameter per second is 22.369363 miles per hour.

df.avgSpeed = df.avgSpeed * 22.369363
df.maxSpeed = df.maxSpeed * 22.369363

df.rename(columns={"avgSpeed": "avgSpeedMPH", "maxSpeed": "maxSpeedMPH"},
          inplace=True)

# Add a column for average pace to the right of average speed.

df.insert(df.columns.get_loc("avgSpeedMPH") + 1, 'avgPaceMPM', 0)

# Pace in minutes per mile is 60/MPH, only set it where avgSpeedMPH > 0.

mask = df.avgSpeedMPH > 0
df.loc[mask, 'avgPaceMPM'] = 60 / df.avgSpeedMPH

# Filter columns to round to two and convert to nullable flaots with NA for 0.

mask = [
    "distanceMiles",
    "avgSpeedMPH",
    "maxSpeedMPH",
    "avgPaceMPM",
]

df[mask] = df[mask].round(2).convert_dtypes().replace(0.0, pd.NA)

# Tennis isn't well integrated into Garmin, so we will augment things here.
# If the name of an activity contains 'tennis' assign it sportType 'TENNIS'

mask = df.name.str.lower().str.contains('tennis')
df.loc[mask, 'sportType'] = "TENNIS"

# Some cycling activities are misclassified as generic, reclassify these

mask = df.name.str.lower().str.contains("cycling")
df.loc[mask, 'sportType'] = "CYCLING"

# Some running activities are misclassified as generic, reclassify these

mask = df.name.str.lower().str.contains("running")
df.loc[mask, 'sportType'] = "RUNNING"

# If the name of an activity contains 'walking' assign it sportType 'WALKING'

mask = df.name.str.lower().str.contains("walking")
df.loc[mask, 'sportType'] = "WALKING"

df.to_pickle("activities.pkl.gz", compression='gzip')
