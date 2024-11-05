# %%
import pandas as pd
import pickle
import os

dir_path = os.path.dirname(__file__)

accel = pd.read_csv(
    dir_path + "/Accelerometer.csv",
    usecols=[1, 2, 3],
    names=["ax", "ay", "az"],
    skiprows=[0],
)
gyro = pd.read_csv(
    dir_path + "/Gyroscope.csv",
    usecols=[1, 2, 3],
    names=["gx", "gy", "gz"],
    skiprows=[0],
)

# %%

combined = pd.concat([accel, gyro], axis=1, join="inner")
pickle.dump(combined, open(dir_path + "/combined.pkl", "wb"))
