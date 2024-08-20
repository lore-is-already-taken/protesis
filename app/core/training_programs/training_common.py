import time
from datetime import datetime

import threading
from adafruit_ads1x15.analog_in import AnalogIn
import pwn
from pwnlib.log import Progress

from app.utils.text_directions import Files


def start_training(interface: AnalogIn, main_file_name: str):
    save_data_route = Files.fileDirection.value + create_file_name(main_file_name)
    print(
        "Realiza los ejercicios de forma calmada y tomate tu tiempo para transisionar entre posiciones"
    )
    instructions = {
        "relaxed_hand": "relaja tu mano y los musculos del brazo testeado",
        "fist_formation": "Cierra lentamente tu mano en un puño. Mantén la muñeca en una posición neutral.",
        "fist_hold": "Mantén la posición del puño, manteniendo todos los dedos y el pulgar firmemente cerrados.",
        "fist_release": "Abre lentamente tu mano, comenzando por liberar el pulgar y luego estirando los dedos para formar una palma abierta.",
        "open_palm": "Mantén tu mano en una posición de palma abierta, con los dedos y el pulgar extendidos pero relajados.",
        "fist_to_open_palm": "Haz la transición de un puño a una palma abierta abriendo lentamente los dedos y estirando la mano.",
        "open_palm_to_fist": "Haz la transición de una palma abierta a un puño cerrando lentamente los dedos y el pulgar para formar un puño firme.",
    }

    exercises = [
        {
            "name": "Relaxed Hand",
            "instructions": "relaxed_hand",
            "duration": 5,
        },
        {
            "name": "Transition to Fist",
            "instructions": "fist_formation",
            "duration": 5,
        },
        {"name": "Fist", "instructions": "fist_hold", "duration": 10},
        {
            "name": "Transition to Relaxed Hand",
            "instructions": "fist_to_open_palm",
            "duration": 5,
        },
    ]
    train_data = pwn.log.progress("Info")
    train_data.status("Vamos a empezar!")
    time.sleep(3)
    count_down(5, train_data)
    train_data.success("Sigue las instruciones")
    for exercise in exercises:
        run_exercise(exercise, instructions, interface, save_data_route)


def run_exercise(exercise, instructions, interface, save_data_route):
    instruction = str(instructions[exercise["instructions"]])
    # print(instruction)
    user_instructions = threading.Thread(
        target=show_instruction, args=(instruction, exercise["duration"])
    )
    user_instructions.start()

    capture_data = threading.Thread(
        target=save_training_data,
        args=(
            interface,
            save_data_route,
            exercise["instructions"],
            exercise["duration"],
        ),
    )
    capture_data.start()

    capture_data.join()
    user_instructions.join()


def save_training_data(sensor: AnalogIn, filename: str, running_instruction, duration):
    """
    this will take the data from the sensor and will save it in the specified route
    """
    file_mode = "a" if file_exists(filename) else "w"
    start_time = time.time()
    with open(filename, file_mode) as f:
        while time.time() - start_time < duration:
            f.write(f"{running_instruction}, {sensor.value},{sensor.voltage}\n")


def file_exists(filename):
    """
    Helper function to check if a file exists
    """
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False


def show_instruction(instruction, duration):
    print(f"\n{instruction}")
    remaining_time = pwn.log.progress("Remaining time")
    count_down(duration, remaining_time)
    remaining_time.success("Vamos a la siguiente prueba")
    time.sleep(2)


def count_down(start, log: Progress):
    while start > 0:
        log.status(start)
        start = start - 1
        time.sleep(1)


def create_file_name(main_name: str) -> str:
    # Obtener la fecha y hora actual
    now = datetime.now()

    # Formatear la fecha y hora según el formato especificado
    formatted_date = now.strftime("%d_%m_%Y_%H_%M")

    # Construir el nombre del archivo
    filename = f"{main_name}_{formatted_date}.txt"

    return filename
