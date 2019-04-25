import os
import pandas as pd

filepath = "fake_attendance_region.csv"
df = pd.read_csv(filepath, sep=",")

print(df.head())
