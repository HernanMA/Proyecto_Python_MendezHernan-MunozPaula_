from Proyecto.menus import Menu_Principal, Menu_Coordinador, Menu_Trainer, menu_reportes
import Proyecto.Modulos.MCamper as CRUDC
import Proyecto.Modulos.MTrainer as CRUDT
import Proyecto.Modulos.MMatriculas as CRUDM
import Proyecto.Modulos.Funciones_salones as CRUDS
import Proyecto.Modulos.Funciones_notas as CRUDN
import Proyecto.Modulos.Modulo_reportes as CRUDR
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
                    CRUDS.crear_salon()
                elif opcion == '7':
                    CRUDS.metercamper_salon()
                elif opcion == '8':
                    CRUDS.mostrar_info_salones
                elif opcion == '9':
                    CRUDN.registrar_notas_filtros()
                elif opcion == '10':
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
                    CRUDT.jornada_trainer()    
                elif opcion == '4':
                    CRUDT.actualizar_trainers()
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")

        elif opcion == '3':
            while True:
                menu_reportes()       
                opcion = input("Seleccione una opción: ")
                system("clear")
                if opcion == '1':
                    CRUDR.Listar_Campers_Inscritos()
                elif opcion == '2':
                    CRUDR.Listar_Campers_Aprobados()
                elif opcion == '3':
                    CRUDR.entrenadores_en_campuslands()
                elif opcion =='4':
                    CRUDR.campers_bajo_rendimiento()
                elif opcion =='5':
                    CRUDR.campers_y_trainers_asociados()
                elif opcion =='6':
                    CRUDR.superaron_y_no_superaron_60()                 
                elif opcion == '7':
                    break
                else:
                    print("Opción inválida. Por favor, seleccione una opción válida.")    
        elif opcion == '4':
            print("¡Hasta luego usuario! ")
            break    
        else:
            print("la opcion ingresada no es válida, por favor ingresa una de las opciones disponibles. ")     

if __name__ == "__main__":
    main()