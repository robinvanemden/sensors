# T-HiGrow Dashboard

The sample code is based on the **[LilyGO T-HiGrow](https://www.aliexpress.com/item/32815782900.html)** multi-sensor board, which gets the on-board sensor data and uploads it to **[Cayenne](https://cayenne.mydevices.com/)**.

Find an example of a live dashbord [here](https://cayenne.mydevices.com/shared/5f5d15c82130755bb2a55562/project/e9af04f1-b554-4317-b4fb-5e5d4d831b7d).

![](image/1.jpg)

# Steps:
1. Install [Visual Studio Code](https://code.visualstudio.com/) on your pc, Install PlatformIO in the extension, or you can install [PlatformIO IDE](https://platformio.org/platformio-ide),it's built on top of [Microsoft's Visual Studio Code](https://code.visualstudio.com/)
2. Set the Cayenne authentication info to match the authentication info from the Dashboard.If you don't have an account, then [create an account](https://accounts.mydevices.com/auth/realms/cayenne/login-actions/registration?client_id=cayenne-web-app&tab_id=01AaoLwmlng)
3. After logging in, you will see the dashboard, click **Add new** in the upper left,Choose **Generic ESP8266**,Then you can see the MQTT username, password and ID you need to use.
4. Fill out the username, password and ID fields in `main.cpp` [here](https://github.com/robinvanemden/sensors/blob/d34218e337a78562e73d7c52e8f850a2deed7dfb/higrow/src/main.cpp#L40-L42).
5. Fill out a WIFI username and password in `main.cpp` [here](https://github.com/robinvanemden/sensors/blob/d34218e337a78562e73d7c52e8f850a2deed7dfb/higrow/src/main.cpp#L36-L37).
6. For my HiGrow device, I needed to calibrate the soil humidity sensor (using a glass of water and a towel to simumlate dry and wet conditions) by changing the values of the [map()](https://www.arduino.cc/reference/en/language/functions/math/map/) function [here](https://github.com/robinvanemden/sensors/blob/b02a2c22a9c39578a9b755197406ee902e8a7c21/higrow/src/main.cpp#L129). It seems that the soil humidity and salt sensors are relatively fragile in the HiGrow.
7. In `platformio.ini` you need to change the virtual COM port number that your HiGrow has connected to on your computer [here](https://github.com/robinvanemden/sensors/blob/c22cb0bfc83a89df9d313deb7242018ab47bb622/higrow/platformio.ini#L18-L19)
8. Compile and upload the sketch.(The arrow at the bottom left of the IDE editor)
9. A temporary widget will be automatically generated in the Cayenne Dashboard. To make the widget permanent click the plus sign on the widget.
