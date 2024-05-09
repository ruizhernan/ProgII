def agregar_tarea(lista_de_tareas, tarea): #Funcion para agregar una tarea, recibe la lista y la tarea nueva
    lista_de_tareas.append(tarea)#Metodo para agregar un elemento a la lista
    print("Tarea agregada:", tarea)

def eliminar_tarea(lista_de_tareas, indice): #Funcion para eliminar un tarea, recibe la lista y el indice seleccionado
    if 0 <= indice < len(lista_de_tareas):
        tarea_eliminada = lista_de_tareas.pop(indice) #Metodo para eliminar segun indice
        print("Tarea eliminada:", tarea_eliminada)
    else:
        print("Índice fuera de rango. No se pudo eliminar la tarea.")

def mostrar_tareas(lista_de_tareas): #Funcion para mostrar las tareas, recibe la lista
    if lista_de_tareas:
        print("Lista de tareas:")
        for indice, tarea in enumerate(lista_de_tareas): #Enumera las tareas de la lista
            print(f"{indice + 1}. {tarea}")
    else:
        print("La lista de tareas está vacía.")
