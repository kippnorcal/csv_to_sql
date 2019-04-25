import argparse
import os
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="file path of csv to parse")
args = parser.parse_args()
filepath = args.filepath

df = pd.read_csv(filepath, sep=",")
print(df.head())
