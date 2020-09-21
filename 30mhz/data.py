# -*- coding: utf-8 -*-

"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Reads a .csv file as exported from the 30Mhz Zensie dashboard.
    into a Python Pandas DataFrame.

"""


import pandas as pd


def read(file):

    # --- import data ---

    # Import csv file containing all sensor readings into a pandas dataframe.
    sensor_df = pd.read_csv(file)
    # Last two rows do not contain data. Delete the.
    sensor_df = sensor_df.head(-2)
    # Rename the first column "timestamp".
    sensor_df.rename(columns={sensor_df.columns[0]: "timestamp"}, inplace=True)
    # Convert the first column to datetime.
    sensor_df["timestamp"] = pd.to_datetime(sensor_df["timestamp"], format="%Y-%m-%d %H:%M:%S")
    # Fix first column type.
    sensor_df.iloc[:, 1] = sensor_df.iloc[:, 1].astype(float)

    return sensor_df


def printer(data):
    print(data)
    print(data.dtypes.to_markdown())


if __name__ == '__main__':
    df = read("data/one-week-every-hour.csv")
    printer(df)
