import json
from os import system

def registrar_trainer():
    with open("Proyecto/trainers.json", "r") as outfile:
        Proyect = json.load(outfile)


    nuevo_trainer = {}
    ultimo_id = max([trainer["ID"] for trainer in Proyect["Trainers"]], default=0)
    nuevo_id = ultimo_id + 1
    nuevo_trainer["ID"] = nuevo_id
    nuevo_trainer["N_documento"] = input("Ingrese el numero de documento del nuevo trainer: ")
    nuevo_trainer["nombre"] = input("Ingrese el primer nombre del nuevo trainer: ")
    nuevo_trainer["apellido"] = input("Ingrese el primer apellido del nuevo trainer: ")
    nuevo_trainer["N_celular"] = input("Ingrese el numero de celular del nuevo trainer: ")
    nuevo_trainer["Horario"] = "No asignado"

    Proyect["Trainers"].append(nuevo_trainer)

    with open("Proyecto/trainers.json", "w") as outfile:
        json.dump(Proyect, outfile, indent=4)

def mostrar_info_trainers():
    with open("Proyecto/trainers.json", "r") as outfile:
        Proyect = json.load(outfile)

        trainers = Proyect["Trainers"]
        while True:
            try:
                ID_trainer = int(input("Ingresa el id del Trainer del que quieras ver la información: "))
                print("\n")

                for trainer in trainers: 
                    if trainer["ID"] == ID_trainer:
                        for key, value in trainer.items():
                            print(f"{key}: {value}")
                        print("\n")    
            except ValueError:
                print("\nPor favor ingrese un  valor numerico")            
            break    
    

def jornada_trainer():
    with open("Proyecto/Trainers.json", "r") as outfile:
        Data = json.load(outfile)

    trainers = Data["Trainers"]
    while True:
        try:
            ID_trainer = int(input("Ingrese el ID del trainer al cual desea asignarle un horario: "))
            for trainer in trainers:
                if trainer["ID"] == ID_trainer:
                    print("\nJornadas:")
                    print("1. Mañana (6:00 a.m - 2:00 p.m)")
                    print("2. Tarde (2:00 p.m - 10:00 p.m)")
                    
                    opcion = input("Seleccione la jornada que desea asignar: ")
                    system("clear")

                    if opcion == '1':
                        jornada = "Manana"
                        trainer["Jornada"] = jornada
                    elif opcion == '2':
                        jornada = "Tarde"
                        trainer["Jornada"] = jornada
                    else:
                        print("Ingrese una opción válida")
        except ValueError:
            print("\nIngrese un valor numérico")
        break

    with open("Proyecto/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)

def actualizar_trainers():
    editacion = open("Proyecto/Trainers.json")
    Data = json.load(editacion)
    trainers = Data["Trainers"]
    ID_trainer = int(input("Ingresa el id del trainer que quieras actualizar: "))
    for trainer in trainers:
        if trainer["ID"] == ID_trainer:
            
            N_documento = input("Ingresa el nuevo numero de documento: ")
            nombre = input("Ingresa el nuevo primer nombre: ") 
            apellido = input("Ingresa el nuevo apellido: ")
            N_celular = input("Ingresa el nuevo numero de celular: ")
            
            trainer["N_documento"] = N_documento
            trainer["nombre"] = nombre
            trainer["apellido"] = apellido
            trainer["N_celular"] = N_celular
    
    with open("Proyecto/Trainers.json", "w") as outfile:
        json.dump(Data, outfile, indent=4)        


        
        

    

        
        

    
