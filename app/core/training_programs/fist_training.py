import time

import pwn

from app.core.training_programs.training_common import create_file_name, start_training
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
## [open_palm, 963, 0.161625]
## [transition_open_palm, 963, 0.161625]
## [relaxed, 963, 0.161625]


def testSensor(test_information, sensor_interface):
    startTime = time.time()
    while time.time() - startTime < 5:
        test_information.status(f"{(time.time() - startTime):.1f}")

        # test_information.status(
        #     f"sensor voltage: {sensor_interface.voltage}\nsensor analog: {sensor_interface.value}"
        # )

    test_information.success("Prueba terminada")


def fistTrain():
    sensorValidator = get_content(Files.sensorValidation.value)
    print(sensorValidator)
    fileName = create_file_name(FILE_CORE_NAME)

    try:
        # getting interface
        # interface = gpio_interface.get_interface()
        interface = ""
        test_information = pwn.log.progress("Sensor data")

        # This is for testing purposes
        testSensor(test_information, interface)
        start_training(interface)

    except Exception as e:
        print("no interface detected")
        raise e
