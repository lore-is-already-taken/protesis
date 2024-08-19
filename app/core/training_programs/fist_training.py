import time

import pwn

from app.hardware import gpio_interface
from app.utils.reader import get_content
from app.utils.text_directions import Files

FILE_CORE_NAME = "FIST_TRAINING"

### the data that will be saved must have this format
### [
### {{ hand status [
##          relaxed,
##          open_palm,
##          fist,
##          transition_fist,
##          transition_open_palm
##          ],
##          AnalogValue,
##          voltaje }}]
## ej:
## [relaxed, 963, 0.161625]


def fistTrain():
    sensorValidator = get_content(Files.sensorValidation.value)
    print(sensorValidator)
    try:
        startTime = time.time()
        # getting interface
        # interface = gpio_interface.get_interface()
        test_sensor = pwn.log.progress("Sensor data")
        while time.time() - startTime < 5:
            # print("AnalogValue: ", interface.value, "Voltage: ", interface.voltage)
            test_sensor.status(time.time() - startTime)
            time.sleep(0.2)
        print("si todo funciona bien, sigamos con la captura de datos", end="\n")

    except Exception as e:
        print("no interface detected")
        raise e
