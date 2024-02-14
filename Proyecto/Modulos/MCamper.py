import json

CAMPER_FIELDS = [
    "número de documento",
    "nombre",
    "segundo nombre",
    "primer apellido",
    "segundo apellido",
    "ciudad",
    "dirección",
    "nombre del acudiente",
    "número telefónico",
    "número fijo",
]

def load_proyect():
    with open("Proyecto/campers.json", "r") as outfile:
        return json.load(outfile)

def save_proyect(proyect):
    with open("Proyecto/campers.json", "w") as outfile:
        json.dump(proyect, outfile, indent=4)

def agregar_camper():
    proyect = load_proyect()
    nuevo_camper = {}
    ultimo_id = max([camper["ID"] for camper in proyect["Campers"]], default=0)
    nuevo_camper["ID"] = ultimo_id + 1
    for field in CAMPER_FIELDS:
        nuevo_camper[field] = input(f"Ingrese {field} del nuevo camper: ")
    nuevo_camper["Estado"] = "Inscrito"
    proyect["Campers"].append(nuevo_camper)
    save_proyect(proyect)

def mostrar_info_campers():
    proyect = load_proyect()
    ID_camper = int(input("Ingresa el id del Camper del que quieras ver la información: "))
    print("\n")
    for camper in proyect["Campers"]: 
        if camper["ID"] == ID_camper:
            for key, value in camper.items():
                print(f"{key}: {value}")
            print("\n")

def actualizar_campers():
    proyect = load_proyect()
    ID_camper = int(input("Ingresa el id del Camper que quieras actualizar: "))
    for camper in proyect["Campers"]:
        if camper["ID"] == ID_camper:
            for field in CAMPER_FIELDS:
                camper[field] = input(f"Ingrese el nuevo {field}: ")
    save_proyect(proyect)


def prueba_inicial():
    with open("Proyecto/campers.json", "r") as outfile:
        Proyect = json.load(outfile)
        Campers = Proyect["Campers"]

    while True:
        try:
            ID_camper = int(input("Ingresa el id del Camper del cual deseas ingresar la nota de su prueba inicial: "))
            for camper in Campers:
                if camper["ID"] == ID_camper:
                    while True:
                        try:
                            nota_practica = int(input("Ingrese la nota práctica de la prueba inicial: "))
                            if 0 <= nota_practica <= 100:
                                while True:
                                    try:
                                        nota_teorica = int(input("Ingrese la nota teórica de la prueba inicial: "))
                                        if 0 <= nota_teorica <= 100:
                                            nota_ingreso = nota_practica + nota_teorica / 2
                                            if nota_ingreso >= 60:
                                                camper["Estado"] = "En proceso de ingreso"
                                            else:
                                                camper["Estado"] = "Reprobado"
                                            break  
                                        print("Nota no válida, ingresa un valor de 0 a 100")
                                    except ValueError:
                                        print("Por favor, ingresa un valor numérico.")
                                break  
                            else:
                                print("Nota no válida, ingresa un valor de 0 a 100")
                        except ValueError:
                            print("Por favor, ingresa un valor numérico.")
                    break  
            break  
        except ValueError:
            print("Por favor, ingresa un valor numérico para el ID del Camper.")

    with open("Proyecto/campers.json", "w") as outfile:
        json.dump(Proyect, outfile, indent=4)