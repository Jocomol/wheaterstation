from wsPart import WsPart
import os
import sys
from w1thermsensor import W1ThermSensor
import datetime


class Thermo(WsPart, W1ThermSensor):

    def __init__(self, logger):
        WsPart.__init__(self, logger)  # Calls the wsPart constructor
        W1ThermSensor.__init__(
            self,
            W1ThermSensor.THERM_SENSOR_DS18B20,
            "00000833e8ff")  # TODO

    def read_measurement(self):
        self.logger.info("Meassuring started")
        meassuered_data = [str(datetime.datetime.now().isoformat())]
        meassuered_temps = (self.get_temperatures([
            self.DEGREES_C,
            self.DEGREES_F,
            self.KELVIN]))
        meassuered_data.append(meassuered_temps[0])
        meassuered_data.append(meassuered_temps[1])
        meassuered_data.append(meassuered_temps[2])
        self.logger.info(
            "Meassured Temperatures: " +
            str(meassuered_data))
        return meassuered_data
