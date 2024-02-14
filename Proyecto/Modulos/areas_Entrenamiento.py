import json
from os import system
def menu_rutas():
    print("\nRutas disponibles:")
    print("1. Ruta NodeJS")
    print("2. Ruta Java")
    print("3. Ruta NetCore")
    opcion = input("Seleccione el número correspondiente a la ruta a asignar: ")
    system("clear")

    if opcion == '1':
        return "NodeJS"
    elif opcion == '2':
        return "Java"
    elif opcion == '3':
        return "NetCore"
    else:
        print("Ingrese una opción válida")
        return menu_rutas()

def menu_areas():
    print("""\n
        ________________________________________  
        |Areas de entrenamiento disponibles: ")|
        |                                      |
        |   1. Sputnik                         |
        |   2. Artemis                         |
        |   3. Apolo                           |
        |______________________________________|
        """)
    opcion = input("Seleccione el area de entrenamiento: ")
    system("clear")

    if opcion == '1':
        return "Sputnik"
    elif opcion == '2':
        return "Artemis"
    elif opcion == '3':
        return "Apolo"
    else:
        print("Ingrese una opción válida")
        return menu_areas()

def Crear_Area():
    with open("Proyecto/zonas_Entrenamientos.json", "r") as file:
        proyect = json.load(file)

    nuevo_Area = {}
    ultimo_id = max([Area["Id"] for Area in proyect["Areas"]], default=0) + 1
    nuevo_Area["Id"] = ultimo_id
    nuevo_Area["nombre del grupo"] = input("Ingrese el nombre del salón: ")

    with open("Proyecto/trainers.json", "r") as file:
        trainers_proyect = json.load(file)["Trainers"]

    while True:
        try:
            id_trainer = int(input("Ingrese el ID del Trainer que se encargará de este salón: "))
            for trainer in trainers_proyect:
                if trainer["ID"] == id_trainer:
                    nuevo_Area["Trainer_encargado"] = trainer["nombre"]
                    nuevo_Area["Horario_de_grupo"] = trainer["Horario"]
                    break
            else:
                print("El ID del Trainer no existe. Por favor, ingrese un ID válido.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico.")

    nuevo_Area["Ruta"] = menu_rutas()
    nuevo_Area["Area"] = menu_areas()
    proyect["Areas"].append(nuevo_Area)

    with open("Proyecto/zonas_Entrenamiento.json", "w") as file:
        json.dump(proyect, file, indent=4)