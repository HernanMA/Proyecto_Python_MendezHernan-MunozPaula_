import json

def matriculas():
    with open("Proyecto/inscritos_Campers.json", "r") as file:
        inscritos = json.load(file)

    with open("Proyecto/campers_Aprobados.json", "r") as file:
        aprobados = json.load(file)

    with open("Proyecto/campers_Reprobados.json", "r") as file:
        reprobados = json.load(file)

    with open("Proyecto/grupos.json", "r") as file:
        grupos = json.load(file)

    with open("Proyecto/salon_Grupos.json", "r") as file:
        salones = json.load(file)

    inscritos = inscritos["Campers"]
    aprobados = aprobados["Aprobados"]
    reprobados = reprobados["Reprobados"]
    grupos = grupos["Grupos"]

    campers_Mover = int(input("Ingrese el ID del camper que desea matricular: "))
    
    for i in range(len(inscritos)):
        if inscritos[i]['ID'] == campers_Mover:
            
            nota_practica = int(input("Ingrese la nota práctica de la prueba inicial: "))
            nota_teorica = int(input("Ingrese la nota teórica de la prueba inicial: "))
            nota_ingreso = (nota_practica + nota_teorica) / 2
            
            if nota_ingreso >= 60:
                inscritos[i]["Estado"] = "Aprobado"
                aprobados.append(inscritos[i])
                with open("Proyecto/campers_Aprobados.json", "w") as outfile:
                    json.dump({"Aprobados": aprobados}, outfile, indent=4)
                   
            else:
                inscritos[i]["Estado"] = "Reprobado"
                reprobados.append(inscritos[i])
                with open("Proyecto/campers_Reprobados.json", "w") as outfile:
                    json.dump({"Reprobados": reprobados}, outfile, indent=4)
                     
