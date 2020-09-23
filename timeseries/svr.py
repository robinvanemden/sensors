# -*- coding: utf-8 -*-

"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Example minimal Support Vector Regression model.
    Predicts humidity from temperature.

"""

import matplotlib.pyplot as plt
from sklearn.svm import SVR
import numpy as np

import data

# --- import data ---

sensor_df = data.read("data/one-month-every-5-minutes.csv")
data.printer(sensor_df)

# --- sensor data  ---

sensor_df["temp"] = sensor_df["Sensor kas 4 R (888) - Temperature (°C) - averages"]
sensor_df["humid"] = sensor_df["Sensor kas 4 R (888) - Humidity (%) - averages"]

# retrieve hours, days
sensor_df['hour'] = sensor_df.timestamp.dt.hour
sensor_df['day'] = sensor_df.timestamp.dt.day

# limit to a week
sensor_df = sensor_df.loc[(sensor_df.day >= 1) & (sensor_df.day < 16)]

states = sensor_df[["temp", "humid"]].copy()

states = states.dropna()

X = states[["temp"]].values
y = states[["humid"]].values

# ---- Optional: feature scaling ---

# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# sc_y = StandardScaler()s
# X = sc_X.fit_transform(X)
# y = sc_y.fit_transform(y)

# ---- Fit SVR ---

# The most important SVR parameter is Kernel type.
# It can be linear,polynomial or gaussian SVR.
# Here we select RBF(a Gaussian type) kernel.
regressor = SVR()

# Fitting the Support Vector Regression Model to the dataset
regressor.fit(X, y.ravel())

# Predicting a new result
y_pred = regressor.predict([[1]])
print(y_pred)

# ---- Plot SVR results ---

# Plotting Support Vector Regression
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X_grid, regressor.predict(X_grid), color="blue")
plt.title("SVR: Temperature / Humidity")
plt.xlabel("Temperature (C)")
plt.ylabel("Humidity (%)")

plt.show()
