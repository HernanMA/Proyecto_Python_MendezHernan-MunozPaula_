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
    print("\nAreas de entrenamiento disponibles: ")
    print("1. Sputnik")
    print("2. Artemis")
    print("3. Apolo")
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

def crear_salon():
    with open("Proyecto/Salones.json", "r") as file:
        data = json.load(file)

    nuevo_salon = {}
    ultimo_id = max([salon["Id"] for salon in data["Salones"]], default=0) + 1
    nuevo_salon["Id"] = ultimo_id
    nuevo_salon["nombre del grupo"] = input("Ingrese el nombre del salón: ")
    nuevo_salon["Ruta"] = menu_rutas()
    nuevo_salon["Salon"] = menu_areas()
    nuevo_salon["Fecha de inicio"] = input("Ingrese la fecha de inicio del grupo: ")
    nuevo_salon["Fecha de finalizacion"] = input("Ingrese la fecha de finalización del grupo: ")

    with open("Proyecto/Trainers.json", "r") as file:
        trainers_data = json.load(file)["Trainers"]

    while True:
        try:
            id_trainer = int(input("Ingrese el ID del Trainer que se encargará de este salón: "))
            for trainer in trainers_data:
                if trainer["ID"] == id_trainer:
                    while True:
                        if trainer["Jornada"] == "Mañana":
                            print("Elige uno de los dos horarios disponibles para la jornada en la que el trainer está disponible:\n ")
                            print("1. 6:00 am - 10:00 am")
                            print("2. 10:00 am - 2:00 pm")
                            eleccion = input("Seleccione una opción: ")
                            if eleccion == '1':
                                horario = "6:00 am - 10:00 am"
                                nuevo_salon["Horario"] = horario
                                break
                            elif eleccion == '2':
                                horario = "10:00 am - 2:00 pm"
                                nuevo_salon["Horario"] = horario
                                break
                            else:
                                print("Opción no válida")           
                        elif trainer["Jornada"] == "Tarde":
                            print("Elige uno de los dos horarios disponibles para la jornada en la que el trainer está disponible:\n ")
                            print("1. 2:00 pm - 6:00 pm")
                            print("2. 6:00 pm - 10:00 pm")
                            eleccion = input("Seleccione una opción: ")
                            if eleccion == '1':
                                horario = "2:00 pm - 6:00 pm"
                                nuevo_salon["Horario"] = horario
                                break
                            elif eleccion == '2':
                                horario = "6:00 pm - 10:00 pm"
                                nuevo_salon["Horario"] = horario
                                break
                            else:
                                print("Opción no válida")        

                    for salon_existente in data["Salones"]:
                        if "Trainer_encargado" in salon_existente and salon_existente["Trainer_encargado"] == trainer["nombre"] and salon_existente["Horario"] == nuevo_salon["Horario"] and salon_existente["Salon"] == nuevo_salon["Salon"]:
                            print("\nEl entrenador ya tiene un grupo en este horario y salón.")
                            break
                        if "Trainer_encargado" in salon_existente and salon_existente["Trainer_encargado"] == trainer["nombre"] and salon_existente["Horario"] == nuevo_salon["Horario"]:
                            print("\nEl entrenador ya tiene un grupo en este horario.")
                            break
                    else:
                        nuevo_salon["Trainer_encargado"] = trainer["nombre"]
                        data["Salones"].append(nuevo_salon)
                        break
            break
        except ValueError:
            print("\nPor favor, ingrese un valor numérico.")

    nuevo_salon["Campers_registrados"] = []        

    with open("Proyecto/Salones.json", "w") as file:
        json.dump(data, file, indent=4)


def cargar_datos():
    with open("Proyecto/campers_Aprobados.json", "r") as file:
        data_campers = json.load(file)
    with open("Proyecto/Salones.json", "r") as file:
        data_salones = json.load(file)
    return data_campers, data_salones

def guardar_datos(data_salones):
    with open("Proyecto/Salones.json", "w") as file:
        json.dump(data_salones, file, indent=4)

def metercamper_salon():
    data_campers, data_salones = cargar_datos()
    campers = data_campers["Aprobados"]
    salones = data_salones["Salones"]
    
    campers_registrados = set()
    for salon in salones:
        for camper in salon.get("Campers_registrados", []):
            campers_registrados.add(camper["ID"])

    while True:
        try:
            id_camper = int(input("Ingresa el ID del Camper al que quieres inscribir a uno de los grupos: "))
            print("\n")
            if id_camper in campers_registrados:
                print("Este Camper ya está inscrito en otro grupo.\n")
                break
            
            camper_encontrado = next((camper for camper in campers if camper["ID"] == id_camper), None)
            if camper_encontrado is None:
                print("No se encontró ningún Camper con el ID ingresado.\n")
                break
            
            if camper_encontrado["Estado"] != "Aprobado":
                print("El estado del Camper no permite la inscripción en ningún grupo.\n")
                break
            
            id_grupo = int(input("Ingresa el ID del grupo en el cual el Camper será inscrito: "))
            print("\n")
            salon_encontrado = next((salon for salon in salones if salon["Id"] == id_grupo), None)
            if salon_encontrado is None:
                print("No se encontró ningún grupo con el ID ingresado.\n")
                break
            
            if len(salon_encontrado.get("Campers_registrados", [])) >= 33:
                print("El grupo ya tiene el máximo de campers inscritos.\n")
                break
            
            if any(camper["ID"] == id_camper for camper in salon_encontrado.get("Campers_registrados", [])):
                print("El Camper ya está registrado en este grupo.\n")
                break
            
            if "Campers_registrados" not in salon_encontrado:
                salon_encontrado["Campers_registrados"] = []
            salon_encontrado["Campers_registrados"].append({
                "ID": camper_encontrado["ID"],
                "número de documento": camper_encontrado["número de documento"],
                "nombre": camper_encontrado["nombre"],
                "primer apellido": camper_encontrado["primer apellido"]
            })
            
            campers_registrados.add(id_camper)
            guardar_datos(data_salones)
            print("El Camper ha sido inscrito exitosamente en el grupo.")
            break
        except ValueError:
            print("\nIngrese un ID válido.")
            
def mostrar_info_salones():
    try:
        with open("Proyecto/Salones.json", "r") as outfile:
            data = json.load(outfile)
            salones = data["Salones"]
        
        id_salon = int(input("Ingresa el ID del salón del que quieres ver la información: "))
        print("\n")
        
        salon_encontrado = next((salon for salon in salones if salon["Id"] == id_salon), None)
        
        if salon_encontrado:
            for key, value in salon_encontrado.items():
                print(f"{key}: {value}")
            print("\n")
            
            campers_registrados = salon_encontrado.get("Campers_registrados", [])
            if campers_registrados:
                print("Campers registrados:")
                for camper in campers_registrados:
                    for key, value in camper.items():
                        print(f"{key}: {value}")
                    print("\n")
            else:
                print("No hay campers registrados en este salón.")
        else:
            print("No se encontró ningún salón con el ID ingresado.")
    except ValueError:
        print("\nPor favor, ingresa un valor válido.")         