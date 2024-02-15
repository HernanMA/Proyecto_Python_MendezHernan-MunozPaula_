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
            | 3. Menú de reportes                |
            | 4. Salir                           |
            |====================================|
        """)

def Menu_Trainer (): 
    from colorama import Fore
    print(Fore.GREEN + """
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
            | 5. Matricular camper               |
            | 6. Crear salón                     |
            | 7. Ingresar camper a un salón      |
            | 8. Mostrar información de grupos   |
            | 9. Registrar notas de modulos      |
            | 10. Exit                           |
            |====================================|
        """)
def menu_reportes(): 
    from colorama import Fore
    print(Fore.WHITE + """
            |====================================|
            |            MENÚ REPORTES           |
            |====================================|
            | 1. Listar campers inscritos        |
            | 2. Lista de campers que pasaron    |
            |    el examen inicial               |
            | 3. Lista de trainers que           |
            |    trabajan en campus              |
            | 4. Lista campers de bajo           |
            |    rendimiento                     |
            | 5. Trainers y campers que están    |
            |    en una ruta                     |
            | 6. Lista de los campers que        |
            |    perdieron y aprobaron en        |
            |    los modulos                     |
            | 7. Exit                           |
            |====================================|
        """)
    





