import time
from datetime import datetime

import pwn


def start_training(interface):
    train_data = pwn.log.progress("Instructions")

    start_time = time.time()
    train_data.status("Relaja la mano")

    while time.time() - start_time < 5:
        train_data.status(time.time() - start_time)


def save_training_data():
    pass


def create_file_name(main_name: str) -> str:
    # Obtener la fecha y hora actual
    now = datetime.now()

    # Formatear la fecha y hora según el formato especificado
    formatted_date = now.strftime("%d_%m_%Y_%H_%M")

    # Construir el nombre del archivo
    filename = f"{main_name}_{formatted_date}.txt"

    return filename
