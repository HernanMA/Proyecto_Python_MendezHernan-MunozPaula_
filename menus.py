def Menu_Principal(): 
    from colorama import Fore
    print(Fore.RED + """
            |====================================|
            |            MENÚ PRINCIPAL          |
            |====================================|
            | 1. Coordinador                     |
            | 2. Trainer                         |
            | 3. Camper                          |
            | 4. Salir                           |
            |====================================|
        """)
    
    print ("")
    print ("=====================================")
    opc = int(input("\n Ingrese la opcion que desea usar : "))
    print ("")
    print ("===================================== ")
    print ("")
    return opc 

def Menu_Trainer (): 
    from colorama import Fore
    print(Fore.YELLOW + """
            |====================================|
            |            MENÚ TRAINER            |
            |====================================|
            | 1. Ver Campers y Salón             |
            | 2. Asignar Notas                   |
            | 3. Salir                           |
            |====================================|
        """)

def Menu_Camper() : 
    print("""
            |====================================|
            |           MENÚ ESTUDIANTE          |
            |====================================|
            | 1. Ver Mi Horario                  |
            | 2. Ver Mis Notas                   |
            | 3. Consultar Mi Estado             |
            | 4. Salir                           |
            |====================================|
        """)
    
def Menu_Coordinador (): 
    from colorama import Fore
    print(Fore.BLUE + """
            |====================================|
            |          MENÚ DEL COORDINADOR      |
            |====================================|
            | 1. Listas Campers/Trainers         |
            | 2. Registrar Campers/Trainers      |
            | 3. Asignar Notas                   |
            | 4. Rutas                           |
            | 5. Matriculas                      |
            | 6. Salir del Sistema               |
            |====================================|
        """)
    
    print ("")
    print ("=====================================")
    opc = int(input("\n Ingrese la opcion que desea usar : "))
    print ("")
    print ("===================================== ")
    print ("")
    return opc 


    

