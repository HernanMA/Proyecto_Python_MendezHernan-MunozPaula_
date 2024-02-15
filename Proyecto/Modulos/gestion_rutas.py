import json

def agregar_estudiante(ruta, estudiante):
    with open("rutas.json", "r") as file:
        rutas = json.load(file)

    # Verifica si la ruta existe y si hay espacio disponible
    if ruta in rutas and len(rutas[ruta]) < 33:
        rutas[ruta].append(estudiante)
        with open("rutas.json", "w") as file:
            json.dump(rutas, file, indent=4)
        print(f"Estudiante {estudiante} agregado a la ruta {ruta}.")
    else:
        print(f"No se pudo agregar al estudiante {estudiante} a la ruta {ruta}.")

def agregar_ruta(ruta):
    with open("rutas.json", "r") as file:
        rutas = json.load(file)

    # Verifica si la ruta ya existe
    if ruta not in rutas:
        rutas[ruta] = []
        with open("rutas.json", "w") as file:
            json.dump(rutas, file, indent=4)
        print(f"Ruta {ruta} agregada.")
    else:
        print(f"La ruta {ruta} ya existe.")
