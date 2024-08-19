from app.core.training_programs.fist_training import fistTrain
from app.core.training_programs.index_Training import indexTrain
from app.utils.reader import get_content
from app.utils.text_directions import Files
from resources.ascii import projectName


def menu():
    print(projectName.project_name, end="\n\n")
    print("selecciona una opcion de funcionamiento", end="\n")

    print(get_content(Files.menu.value))
    user_response = input("Tu respuesta: ")
    if user_response == "1":
        fistTrain()
    elif user_response == "2":
        indexTrain()
