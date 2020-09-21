"""
    JADS 2020 Data-Driven Food Value Chain course
    Introduction to Sensors

    Lunar Lander Micropython Exercise

"""

# ------------------------  Objective of the game -------------------------------------

# this game simulates a lunar landing module (LLM) landing on the moon
# you are the pilot and need to control how much fuel you burn in the
# retro rockets so that your descent speed slows to zero just as your
# altitude above the moon's surface reaches zero. If you impact the moon
# more than 5 m below the surface, or your speed on impact is
# greater than 5 m/s then you have considered to have crashed.
# Otherwise it is considered to be a 'good' landing.
# If you run out of fuel, LLM will accelerate towards moon by gravity.

# ----------------------------  Assignment --------------------------------------------

# Copy paste this code at https://micropython.org/unicorn/

# Then replace the constant burn rate in line 57 with interpolated input from the ADC slider,
# with some delay from a basic moving average filter (for instance with window of n = 3)

# -----------------------------  Source code  ------------------------------------------

import time
import machine
import pyb

# The slider is connected to pin Y4
y4 = machine.Pin('Y4')

# read out slider through analog to digital converter
adc = pyb.ADC(y4)

# slider_out between 0 - 255
slider_out = adc.read()

# set up the game's initial parameters
speed = 30  # speed approaching the moon
fuel = 1500  # how much fuel is left
altitude = 1000  # altitude above moon
gravity = 1.622  # acceleration due to gravity
burn = 0  # initial rate of burning fuel in retrorockets

# while LLM is above the moon's surface,
# calculate flight data and take input from pilot
while altitude > 0:
    # calculate how long until LLM will impact moon at current speed (impact)
    if speed <= 0:
        impact = 1000
    else:
        impact = altitude / speed
    # display flight data
    print(
        "Altitude={:8.3f} Speed={:6.3f} Fuel={:8.3f} Impact={:6.3f} Previous burn={:6.3f}".format(altitude, speed, fuel,
                                                                                                  impact, burn))
    # take input from pilot

    burn = 5  # <----- replace this line of code with filtered dynamic input from slider

    # ensure rate of fuel burning is within rocket's capability and doesn't exceed remaining fuel
    if burn < 0:
        burn = 0
    if burn > 50:
        burn = 50
    if burn > fuel:
        burn = fuel

    # adjust to change the speed of the game
    time.sleep_ms(300)

    # calculate new flight data
    altitude -= speed
    speed += gravity - burn / 10
    fuel -= burn

# loop has ended so we must have hit moon's surface
# display final flight data and assess whether it was a crash or a good landing
print("Altitude={:8.3f} Speed={:6.3f} Fuel={:8.3f} Last burn={:6.3f}".format(altitude, speed, fuel, burn))
if altitude < - 5 or speed > 5:
    print("You have crashed")
else:
    print("You have landed")
