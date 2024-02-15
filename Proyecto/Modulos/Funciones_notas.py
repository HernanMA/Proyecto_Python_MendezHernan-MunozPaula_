import json
import os

def ingresar_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():  
            return int(valor)
        else:
            print("Por favor, ingrese un valor numérico.")

def ingresar_nota(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():  
            nota = int(valor)
            if 0 <= nota <= 100:
                return nota
            else:
                print("Por favor, ingrese una nota entre 0 y 100.")
        else:
            print("Por favor, ingrese un valor numérico.")

def actualizar_recuento_modulos(notas_data):
    modulos_superaron_60 = 0
    modulos_no_superaron_60 = 0

    for camper_notas in notas_data.values():
        if isinstance(camper_notas, list):  # Verifica si camper_notas es una lista
            for modulo in camper_notas:
                if "nota final del modulo" in modulo:
                    if modulo["nota final del modulo"] >= 60:
                        modulos_superaron_60 += 1
                    else:
                        modulos_no_superaron_60 += 1

    return modulos_superaron_60, modulos_no_superaron_60

def registrar_notas_filtros():
    with open("Proyecto/campers_Aprobados.json", "r") as infile:
        campers_data = json.load(infile)
    campers = campers_data.get("Aprobados", [])
    
    with open("Proyecto/Notas.json", "r") as infile:
        notas_data = json.load(infile)
    
    ID_camper = ingresar_numero("Ingresa el ID del Camper para ingresar las notas: ")

    found_camper = None
    for camper in campers:
        if camper["ID"] == ID_camper and camper["Estado"] == "Aprobado":
            found_camper = camper
            break

    if not found_camper:
        print("Camper no encontrado o no está aprobado.")
        return

    notas = notas_data.get(str(ID_camper), [])

    print("\nMenú de módulos: ")
    print("1. Fundamentos de programacion (Introduccion a la programacion, PSeint y Python) ")
    print("2. Programacion Web (HTML, CSS y Bootstrap) ")
    print("3. Programacion formal (Java, JavaScript, C#) ")
    print("4. Base de datos (MySQL, MongoDB y PostgreSQL) ")
    print("5. Backend (.NET Core, Spring Boot, Node.js y Express) ")

    opcion = ingresar_numero("Seleccione el modulo: ")

    modulo_nombres = {
        '1': "Fundamentos de programacion",
        '2': "Programacion Web",
        '3': "Programacion formal",
        '4': "Base de datos",
        '5': "Backend"
    }

    if str(opcion) not in modulo_nombres:
        print("Opcion invalida.")
        return

    nombre_modulo = modulo_nombres[str(opcion)]

    for nota_modulo in notas:
        if nota_modulo["nombre del modulo"] == nombre_modulo:
            nota_teorica = ingresar_nota("Ingresa el valor de la nota teorica: ")
            nota_practica = ingresar_nota("Ingresa el valor de la nota practica: ")
            nota_trabajos = ingresar_nota("Ingresa el valor de la nota de los trabajos: ")

            nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_trabajos * 0.1)

            nota_modulo["nota final del modulo"] = nota_final

            if nota_final < 60:
                found_camper["Riesgo"] = "Riesgo alto"

            break
    else:
        nota_teorica = ingresar_nota("Ingresa el valor de la nota teorica: ")
        nota_practica = ingresar_nota("Ingresa el valor de la nota practica: ")
        nota_trabajos = ingresar_nota("Ingresa el valor de la nota de los trabajos: ")

        nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (nota_trabajos * 0.1)

        notas.append({
            "nombre del modulo": nombre_modulo,
            "nota final del modulo": nota_final,
        })

        if nota_final < 60:
            found_camper["Riesgo"] = "Riesgo alto"

    # Actualizar la información en el archivo JSON
    notas_data[str(ID_camper)] = notas
    modulos_superaron_60, modulos_no_superaron_60 = actualizar_recuento_modulos(notas_data)
    notas_data["Modulos_superaron_60"] = modulos_superaron_60
    notas_data["Modulos_no_superaron_60"] = modulos_no_superaron_60

    with open("Proyecto/Notas.json", "w") as outfile:
        json.dump(notas_data, outfile, indent=4)

    with open("Proyecto/Campers.json", "w") as outfile:
        json.dump(campers_data, outfile, indent=4)

    print("Notas registradas exitosamente.")