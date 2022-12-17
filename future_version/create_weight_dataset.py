import json
import pandas as pd

json_directory = "/home/rerobbins/garmin_data/DI_CONNECT/DI-Connect-User"
json_file = json_directory + "/user_biometrics.json"

with open(json_file) as f:
    data = json.load(f)

raw_df = pd.json_normalize(data)


# Limit to data from Garmin scale.

mask = raw_df["weight.sourceType"] == "INDEX_SCALE"
df = raw_df[mask]

df = df.set_index(pd.to_datetime(df["metaData.calendarDate"]))
df.index.name = "timeStamp"

# Limit to fields of interest.

mask = [
    "weight.weight",
    "weight.bmi",
    "weight.bodyFat",
    "weight.bodyWater",
    "weight.boneMass",
    "weight.muscleMass",
]

df = df[mask]
df = df.convert_dtypes()

df.rename(columns={
                    "weight.weight": "weightPounds",
                    "weight.bmi": "BMI",
                    "weight.bodyFat": "bodyFatPCT",
                    "weight.bodyWater": "bodyWaterPCT",
                    "weight.boneMass": "boneMassPounds",
                    "weight.muscleMass": "muscleMassPounds",
                    },
          inplace=True)

# Replace zero with pd.NA everywhere

df = df.replace(0, pd.NA)

# Weight is in grams, one pound has 453.59237 grams

df.weightPounds = df.weightPounds / 453.59237
df.boneMassPounds = df.boneMassPounds / 453.59237
df.muscleMassPounds = df.muscleMassPounds / 453.59237

# Round all the numbers (all of which are floats) to two decimal places

df = df.round(2)

df.to_pickle("weight.pkl.gz", compression='gzip')
