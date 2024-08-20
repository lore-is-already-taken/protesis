import time

import pwn

from app.core.training_programs.training_common import create_file_name, start_training
from app.hardware import gpio_interface
from app.utils.reader import get_content
from app.utils.text_directions import Files

FILE_CORE_NAME = "FIST_TRAINING"


def testSensor(test_information, sensor_interface):
    startTime = time.time()
    while time.time() - startTime < 3:
        test_information.status(
            f"sensor voltage: {(sensor_interface.voltage):.3f}\nsensor analog: {sensor_interface.value}"
        )
        time.sleep(0.2)
    test_information.success("Prueba terminada")


def fistTrain():
    sensorValidator = get_content(Files.sensorValidation.value)
    print(sensorValidator)

    try:
        # getting interface
        interface = gpio_interface.get_interface()
        test_information = pwn.log.progress("Sensor data")

        # This is for testing purposes
        testSensor(test_information, interface)
        start_training(interface, FILE_CORE_NAME)

    except Exception as e:
        print("no interface detected")
        raise e
