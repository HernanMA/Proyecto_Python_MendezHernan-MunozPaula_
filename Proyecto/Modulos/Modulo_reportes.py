import json

def Listar_Campers_Inscritos():
    with open("Proyecto/inscritos_Campers.json", "r") as outfile:
        Data = json.load(outfile)
        campers = Data["Campers"]
    print("\n")
    for camper in campers:
        if camper["Estado"] == "Inscrito":
            for key, value in camper.items():
                print(f"{key}: {value}")
        print("\n")

def Listar_Campers_Aprobados():
    with open("Proyecto/campers_Aprobados.json", "r") as outfile:
        Data = json.load(outfile)
        campers = Data["Aprobados"]
    print("\n")
    for camper in campers:
        if camper["Estado"] == "Aprobado":
            for key, value in camper.items():
                print(f"{key}: {value}")
        print("\n")        

def entrenadores_en_campuslands():
    with open("Proyecto/Trainers.json", "r") as outfile:
        Data = json.load(outfile)
    trainers = Data["Trainers"]
        
    print("\n")
    for trainer in trainers:
            for key, value in trainer.items():
                print(f"{key}: {value}")
            print("\n")

def campers_bajo_rendimiento():
    with open("Proyecto/campers_Reprobados.json", "r") as outfile:
        Data = json.load(outfile)
        campers = Data["Reprobados"]
    print("\n")
    for camper in campers:
            for key, value in camper.items():
                print(f"{key}: {value}")
    print("\n")

def campers_y_trainers_asociados():
    with open("Proyecto/Salones.json", "r") as outfile:
        data = json.load(outfile)
        salones = data["Salones"]
        
    for salon in salones:
        ruta = salon["Ruta"]
        nombre_grupo = salon["nombre del grupo"]
        trainer_encargado = salon["Trainer_encargado"]
        campers_registrados = salon["Campers_registrados"]
        
        print("Ruta:", ruta)
        print("Nombre del grupo:", nombre_grupo)
        print("Trainer encargado:", trainer_encargado)
        print("Campers registrados:")
        for camper in campers_registrados:
            print("\tNombre:", camper["nombre"])
            print("\tApellido:", camper["apellido"])
            print("\tNúmero de documento:", camper["N_documento"])
            print()
        print()

def superaron_y_no_superaron_60():
    with open("Proyecto/Notas.json", "r") as file:
        notas_data = json.load(file)
        superaron = notas_data.get("Modulos_superaron_60", 0)
        no_superaron = notas_data.get("Modulos_no_superaron_60", 0)

        print("Modulos superaron 60:", superaron)
        print("Modulos no superaron 60:", no_superaron)

    with open("Proyecto/Salones.json", "r") as file:
        salones_data = json.load(file)
        salones = salones_data.get("Salones", [])

        for salon in salones:
            ruta = salon.get("Ruta", "")
            trainer_encargado = salon.get("Trainer_encargado", "")

            print("Ruta:", ruta)
            print("Trainer encargado:", trainer_encargado)  