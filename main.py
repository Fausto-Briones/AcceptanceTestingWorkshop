tasks = []
completedTasks = []


def addActivity(activity):
    tasks.append(activity)

def markActivity(activity):
   
   if activity not in tasks:
       print("Actividad no encontrada")
       return

   completedTasks.append(activity)
   print(f'''
        Actividades completadas:
         {completedTasks}
    ''') 

def showActivities():
    print(tasks)

def eraseList():
    tasks.clear()

def showPendingActivities():
    print("Actividades pendientes:")
    for actividad in tasks:
        if actividad not in completedTasks:
            print(f'{actividad}')



if __name__ == "__main__":
    user_input = int(input('''Seleccione una de las opciones: 
                      
                       1.- Agregar una actividad
                       2.- Marcar una actividad como completada
                       3.- Ver todas las actividades
                       4.- Borrar toda la lista de actividades
                       5.- Mostrar actividades pendientes
                       6.- Salir
                       '''))

    while user_input != 6:
        if user_input == 1:
            actividad = input("Ingrese una actividad: ")
            addActivity(actividad)
        elif user_input == 2:
            actividad = input("Ingrese una actividad: ")
            markActivity(actividad)
        elif user_input == 3:
            showActivities()
        elif user_input == 4:
            eraseList()
        elif user_input == 5:
            showPendingActivities()

        user_input = int(input('''Seleccione una de las opciones: 
                      
                       1.- Agregar una actividad
                       2.- Marcar una actividad como completada
                       3.- Ver todas las actividades
                       4.- Borrar toda la lista de actividades
                       5.- Mostrar actividades pendientes
                       6.- Salir
                       '''))