import Proyecto.Modulos.MCamper as CRUDC
import Proyecto.Modulos.MTrainer as CRUDT
import Proyecto.Modulos.areas_Entrenamiento as CRUDA
from os import system

def Menu_Principal(): 
    from colorama import Fore
    print(Fore.RED + """
            |====================================|
            |              PERFILES              |
            |====================================|
            |   Por favor selecciona un perfin   |
            |                                    |
            | 1. Perfil de coordinador           |
            | 2. Perfil de Trainers              |
            | 3. Salir                           |
            |====================================|
        """)

def Menu_Trainer (): 
    from colorama import Fore
    print(Fore.YELLOW + """
            |====================================|
            |          PERFIL TRAINER            |
            |====================================|
            | 1. Agregar nuevo trainer           |
            | 2. Mostrar información de trainers |
            | 3. asignar horario del trainer     |
            | 4. Exit                            |
            |====================================|
        """)

def Menu_Coordinador() : 
    from colorama import Fore
    print(Fore.BLUE + """
            |====================================|
            |          PERFIL COORDINADOR        |
            |====================================|
            | 1. Agregar nuevo camper            |
            | 2. Mostrar información de campers  |
            | 3. Actualizar información de       |
            |    campers ya registrados          |
            | 4. Registrar notas prueba de       |
            |    admisión                        |
            | 5. Crear nuevo salón               |
            | 6. Atrás                           |
            |====================================|
        """)

def main():
    while True:
        Menu_Principal()
        opcion = input("Seleccione una opción: ")
        system("clear")
        if opcion == '1':
            while True:
                Menu_Coordinador()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    CRUDC.agregar_camper()
                elif opcion == '2':
                    CRUDC.mostrar_info_campers()
                elif opcion == '3':
                    CRUDC.actualizar_campers()
                elif opcion == '4':
                    CRUDC.prueba_inicial()
                elif opcion == '5':
                    CRUDA.Crear_Area()        
                elif opcion == '6':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")
        elif opcion == '2':
            while True:
                Menu_Trainer()
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    CRUDT.registrar_trainer()
                elif opcion == '2':
                    CRUDT.mostrar_info_trainers()
                elif opcion == '3':
                    CRUDT.horario_trainer()    
                elif opcion == '4':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

        elif opcion == '3':
            print("¡Hasta luego usuario! ")
            break    
        else:
            print("la opcion ingresada no es válida, por favor ingresa una de las opciones disponibles. ")     

if __name__ == "__main__":
    main()
