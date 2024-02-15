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
    with open("Proyecto/inscritos_Campers.json", "r") as outfile:
        return json.load(outfile)

def save_proyect(proyect):
    with open("Proyecto/inscritos_Campers.json", "w") as outfile:
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

def solicitar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingresa un valor numérico.")

def buscar_camper(Campers, ID_camper):
    for camper in Campers:
        if camper["ID"] == ID_camper:
            return camper
    return None

def mostrar_info_campers():
    proyect = load_proyect()
    ID_camper = solicitar_numero("Ingresa el id del Camper del que quieras ver la información: ")
    print("\n")
    camper = buscar_camper(proyect["Campers"], ID_camper)
    if camper is not None:
        for key, value in camper.items():
            print(f"{key}: {value}")
        print("\n")
    else:
        print("Camper no encontrado, por favor ingresa un ID válido.")

def actualizar_campers():
    proyect = load_proyect()
    ID_camper = solicitar_numero("Ingresa el id del Camper que quieras actualizar: ")
    camper = buscar_camper(proyect["Campers"], ID_camper)
    if camper is not None:
        for field in CAMPER_FIELDS:
            camper[field] = input(f"Ingrese el nuevo {field}: ")
        save_proyect(proyect)
    else:
        print("Camper no encontrado, por favor ingresa un ID válido.")


