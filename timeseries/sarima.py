"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Basic Seasonal (S)ARIMA model on PAR Sensor (sunlight) data.

"""

from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import pandas as pd
import data

# --- import data ---

# import data, inspect
sensor_df = data.read("data/330-days-some-sensors-every-hour.csv")

# copy long sensor column name to shorter named column (could also rename, of course)
sensor_df["light"] = sensor_df["PAR Sensor (13D) - PAR (μmol m−2 s−1) - averages"]

# copy just light and timestamp columns
time_series = sensor_df[["timestamp", "light"]].copy()

time_series.set_index('timestamp', inplace=True)

# impute missings
time_series['light'] = time_series['light'].fillna(method="ffill")

# --- seasonal decompose ---

# A timeseries can be decomposed into the following components:
#
# Level: The average value in the series.
# Trend: The increasing or decreasing value in the series.
# Seasonality: The repeating short-term cycle in the series.
# Noise: The random variation in the series.
#
# An additive model suggests that the components are added together as follows:
# y(t) = Level + Trend + Seasonality + Noise

# plot all decomposed components
result = seasonal_decompose(time_series, model='additive', period=24)
result.plot()
plt.show()

# plot 24h seasonal component, zoom in on one days
ax = result.seasonal.plot()
ax.set_xlim(pd.Timestamp('2020-01-01'), pd.Timestamp('2020-01-02'))
ax.set_xlabel('Date')
ax.set_ylabel('PAR Level')
ax.set_title('Seasonal component (24h)')
plt.show()

# --- auto arima ---

# takes up to 20 minutes

#    auto = auto_arima(time_series['light'], m=24,
#                      seasonal=True, trace=True,
#                      error_action="ignore", suppress_warnings=True)

# Best model: ARIMA(0,1,2)(2,0,0)[24] AIC=80295.111


# --- fit seasonal arima ---

model = SARIMAX(time_series['light'], trend='n',
                order=(0, 1, 2), seasonal_order=(2, 0, 0, 24))
results = model.fit()
results.summary()

# --- within sample prediction ---

# predict
pred = results.get_prediction(start='2019-11-01', dynamic=False)
pred_ci = pred.conf_int()

# plot within sample prediction
ax = time_series['light']['2019-11-01':].plot(label='observed')
pred.predicted_mean.plot(ax=ax, label='forecast', alpha=.7)
ax.set_xlim(pd.Timestamp('2019-11-05'), pd.Timestamp('2019-11-06'))
ax.set_ylim(-100, 300)

ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_xlabel('Date')
ax.set_ylabel('PAR Level')
ax.set_title('Within sample prediction')
plt.legend()
plt.show()

# --- out of sample prediction ---

# forecast
index = pd.date_range("2020-09-20 15:00", "2020-09-24 15:00", freq="1h")
forecast = results.get_forecast(steps=len(index), index=index)
forecast_ci = forecast.conf_int()

# plot
ax = time_series['light']['2020-09-16':].plot(label='observed')
forecast.predicted_mean.plot(ax=ax, label='forecast', alpha=.7)

ax.fill_between(forecast_ci.index,
                forecast_ci.iloc[:, 0],
                forecast_ci.iloc[:, 1], color='k', alpha=.2)

ax.set_title('Out of sample prediction')
plt.legend()
plt.show()
