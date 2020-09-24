# -*- coding: utf-8 -*-

"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Minimal Kalman sensor fusion example.

"""

import scipy
import pandas as pd
import pykalman
import numpy as np
import matplotlib.pyplot as plt

import data


# --- import data ---

sensor_df = data.read("data/one-week-every-hour.csv")
data.printer(sensor_df)


# --- plot temperature sensor data ---

# show plot for sensors positioned to the left and right in the greenhouse
sensor_df.plot(x="timestamp", y=["Sensor kas 4 R (888) - Temperature (°C) - averages",
                                 "Sensor kas 4 L (073) - Temperature (°C) - averages"])
plt.show()


# --- kalman filter sensor fusion ---

sensors = 2

states_all = sensor_df[["Sensor kas 4 R (888) - Temperature (°C) - averages",
                        "Sensor kas 4 L (073) - Temperature (°C) - averages"]].copy()

states_initial = states_all.iloc[0, :].copy()

kalman = pykalman.KalmanFilter(transition_matrices=[1.],
                               observation_matrices=np.ones(sensors).reshape(sensors, 1),
                               initial_state_mean=np.mean(states_initial),
                               initial_state_covariance=[1.],
                               observation_covariance=np.eye(sensors))

states, _ = kalman.filter(states_all)
states = states.reshape(states.shape[0])
states = pd.Series(states, index=sensor_df.timestamp)

# --- plot prediction ---

ax = sensor_df.plot(x="timestamp",
                    y=["Sensor kas 4 R (888) - Temperature (°C) - averages"],
                    linestyle="",marker="o", color="b")
ax = sensor_df.plot(x="timestamp", ax=ax,
                    y=["Sensor kas 4 L (073) - Temperature (°C) - averages"],
                    linestyle="",marker="o", color="g", )
states.plot(ax=ax, color="r")
L=plt.legend()
L.get_texts()[0].set_text('observed temp 1')
L.get_texts()[1].set_text('observed temp 2')
L.get_texts()[2].set_text('predicted')
plt.show()
