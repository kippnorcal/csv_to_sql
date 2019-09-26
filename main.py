import argparse
import os

import pandas as pd
from sqlsorcery import MSSQL


parser = argparse.ArgumentParser()
parser.add_argument("--filepath", help="file path of csv to parse")
parser.add_argument("--tablename", help="name of the destination sql able")
args = parser.parse_args()
file = args.filepath
table = args.tablename


def main():
    df = pd.read_csv(file, sep=",")
    sql = MSSQL()
    sql.insert_into(table, df)


if __name__ == "__main__":
    main()
