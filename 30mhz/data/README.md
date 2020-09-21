## 30Mhz Zensie pre-saved data sets

CSV file with one data point per hour for all sensors for a week:

* [one-month-every-5-minutes.csv](one-month-every-5-minutes.csv)

CSV file with one data point every five minutes for all sensors for a month:

* [one-week-every-hour.csv](one-week-every-hour.csv)

CSV file with one data point per hour for some sensors for 330 days:

* [330-days-some-sensors-every-hour.csv](330-days-some-sensors-every-hour.csv)

### Additional sensor information

* [Photosynthetically Active Radiation (PAR) Sensor](https://www.30mhz.com/sensor/photosynthetically-active-radiation-sensor/)

Use the PAR to measure PPFD (Photosynthetic Photon Flux Density) in agricultural environments including greenhouses, 
growth chambers, or outdoor plant canopy environments.

* [Sendot Oxygen and Photosynthesis Sensors](https://www.sendot.nl/our-sensors/)

See also [here](docs/Application-note-2020-EFF-PAR-EN-17-9.pdf): "The light sum the plant receives should enable it to consume all the available (stored) CO2. 
This can be observed as a dip in photosynthesis efficiency.
Continued lighting after this critical moment will lead to stress, damage and productivity loss. 
If the available CO2 is not yet completely consumed, more light can be given to prolong photosynthesis and production."

* [Pointed Micro Climate (PMC) sensor](https://www.30mhz.com/sensor/pointed-micro-climate-sensor/?specs)

* [0013A20041A24464 Soil moisture sensor](https://www.30mhz.com/sensor/soil-moisture-sensor/)

This soil sensor determines volumetric water content (VWC) by measuring the dielectric constant of the medium 
using capacitance and frequency domain technology to provide accurate measurements of all soils and soilless 
medias with a wide range of salinities

ECb (bulk) is the Electrical conductivity the sensor senses inside 
the material (hence bulk).

ECp (pore) is a calculation of the expected Electrical Conductivity 
of the water when it is extracted from the pores of the material (pore water).

* [Overview of all types of 30Mhz Sensors](https://www.30mhz.com/products/sensors/)

### Data dictionary

| Field name  | Type          |
|:---------------------------------------------------------------------------------|:---------------|
| timestamp                                                                        | datetime64[ns] |
| luwe zijde raamstand - %  (afd 4) - Percentage (%) - averages                    | float64        |
| PAR Sensor (13D) - PAR (μmol m−2 s−1) - averages                                 | float64        |
| Weather solutions station Pantar Tuinderij - Air pressure (hPa) - averages       | float64        |
| Weather solutions station Pantar Tuinderij - Global radiation  (W/m2) - averages | float64        |
| Weather solutions station Pantar Tuinderij - Rain (mm) - averages                | float64        |
| Weather solutions station Pantar Tuinderij - Rain probability (%) - averages     | float64        |
| Weather solutions station Pantar Tuinderij - Relative humidity (%) - averages    | float64        |
| Weather solutions station Pantar Tuinderij - Temperature (°C) - averages         | float64        |
| Weather solutions station Pantar Tuinderij - Wind direction () - averages        | float64        |
| Weather solutions station Pantar Tuinderij - Wind speed (m/s) - averages         | float64        |
| vochtdeficit - g/m³  (afd 4) - Humidity deficit (g/m3) - averages                | float64        |
| verwarmingstemp: ber - °C  (afd 4) - Temperature (°C) - averages                 | float64        |
| ventilatietemp: ber  - °C  (afd 4) - Temperature (°C) - averages                 | float64        |
| Tafelbuis - °C  (afd 4) - Temperature (°C) - averages                            | float64        |
| Sensor PMC (21B) - Surface temperature (°C) - averages                           | float64        |
| Sensor PMC (21B) - Absolute Humidity (g/m3) - averages                           | float64        |
| Sensor PMC (21B) - Absolute diff. temp. and dewpoint temp. (°C) - averages       | float64        |
| Sensor PMC (21B) - Dewpoint (°C) - averages                                      | float64        |
| Sensor PMC (21B) - Humidity (%) - averages                                       | float64        |
| Sensor PMC (21B) - Humidity Deficit (g/m3) - averages                            | float64        |
| Sensor PMC (21B) - Air temperature (°C) - averages                               | float64        |
| Sensor PMC (21B) - VPD (kPa) - averages                                          | float64        |
| Sensor kas 4 R (888) - Absolute Humidity (g/m3) - averages                       | float64        |
| Sensor kas 4 R (888) - Dewpoint (°C) - averages                                  | float64        |
| Sensor kas 4 R (888) - Humidity (%) - averages                                   | float64        |
| Sensor kas 4 R (888) - Humidity Deficit (g/m3) - averages                        | float64        |
| Sensor kas 4 R (888) - Temperature (°C) - averages                               | float64        |
| Sensor kas 4 L (073) - Absolute Humidity (g/m3) - averages                       | float64        |
| Sensor kas 4 L (073) - Dewpoint (°C) - averages                                  | float64        |
| Sensor kas 4 L (073) - Humidity (%) - averages                                   | float64        |
| Sensor kas 4 L (073) - Humidity Deficit (g/m3) - averages                        | float64        |
| Sensor kas 4 L (073) - Temperature (°C) - averages                               | float64        |
| Sensor 0013A20041A24464 - ECb (µS/cm) - averages                                 | float64        |
| Sensor 0013A20041A24464 - ECw (µS/cm) - averages                                 | float64        |
| Sensor 0013A20041A24464 - Temp (°C) - averages                                   | float64        |
| Sensor 0013A20041A24464 - VWC (%) - averages                                     | float64        |
| Sendot Zuurstof sensor (5E1) - atmospheric (%) - averages                        | float64        |
| Sendot Zuurstof sensor (5E1) - battery (V) - averages                            | float64        |
| Sendot Zuurstof sensor (5E1) - dissolved (mg/L) - averages                       | float64        |
| Sendot Zuurstof sensor (5E1) - pressure (mB) - averages                          | float64        |
| Sendot Zuurstof sensor (5E1) - saturation (%sat) - averages                      | float64        |
| Sendot Zuurstof sensor (5E1) - temperature (°C) - averages                       | float64        |
| Sendot Fotosynthese efficiency (11B) - battery (V) - averages                    | float64        |
| Sendot Fotosynthese efficiency (11B) - efficiency (%) - averages                 | float64        |
| Sendot Fotosynthese efficiency (11B) - f0 (units) - averages                     | float64        |
| Sendot Fotosynthese efficiency (11B) - fmax (units) - averages                   | float64        |
| Sendot Fotosynthese efficiency (11B) - par (μmol m−2 s−1) - averages             | float64        |
| Schermdoek 1 - %  (afd 4) - Percentage (%) - averages                            | float64        |
| RV kas - %  (afd 4) - Humidity (%) - averages                                    | float64        |
| kastemperatuur - °C  (afd 4) - Temperature (°C) - averages                       | float64        |
| kastemperatuur - °C  (afd 1) - Temperature (°C) - averages                       | float64        |
| bovenbuis - °C  (afd 4) - Temperature (°C) - averages                            | float64        |
| bovenbuis - °C  (afd 1) - Temperature (°C) - averages                            | float64        |
| wind zijde raamstand - %  (afd 4) - Percentage (%) - averages                    | float64        |
| Sensor 0013A20041A0002A NIEUW - co2 (ppm) - averages                             | float64        |

