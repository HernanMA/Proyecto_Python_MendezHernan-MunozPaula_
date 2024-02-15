from Proyecto.menus import Menu_Principal, Menu_Coordinador, Menu_Trainer
import Proyecto.Modulos.MCamper as CRUDC
import Proyecto.Modulos.MTrainer as CRUDT
import Proyecto.Modulos.MMatriculas as CRUDM
import Proyecto.Modulos.gestion_rutas as CRUDR
from os import system

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
                    CRUDM.matriculas()        
                elif opcion == '6':
                    CRUDR.agregar_estudiante()        
                elif opcion == '7':
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
