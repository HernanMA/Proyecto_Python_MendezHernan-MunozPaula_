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

