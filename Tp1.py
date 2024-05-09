#Se importan librerias a utilizar
import os
from lib.Funciones import agregar_tarea, eliminar_tarea, mostrar_tareas

#Se establece una funcion principal (C++ s2)
def main():
    
    #Limpieza de la consola
    os.system("cls")
    #Se establece array para las tareas y control para el ciclo while
    lista_de_tareas = []
    salir = False

      
    while not salir:
        #Comienza bloque de try
        try:
            
            opcion = input("¿Qué acción desea realizar? (agregar, eliminar, mostrar, fin): ")
            #Opciones de repuesta en base a la opcion solicitada
            if opcion.lower() == "fin":
                salir = True
            elif opcion.lower() == "agregar":
                nueva_tarea = input("Ingrese una nueva tarea: ")
                agregar_tarea(lista_de_tareas, nueva_tarea)
            elif opcion.lower() == "eliminar":
                mostrar_tareas(lista_de_tareas)
                indice_a_eliminar = int(input("Ingrese el índice de la tarea que desea eliminar: "))
                eliminar_tarea(lista_de_tareas, indice_a_eliminar - 1) 
            elif opcion.lower() == "mostrar":
                mostrar_tareas(lista_de_tareas)
            else:
                print("Opción no válida. Por favor, elija entre 'agregar', 'eliminar', 'mostrar' o 'fin'.")

        
        except ValueError: #Se establece una excepción del tipo ValueError para verificar el indice utilizado
            print("Error: Debe ingresar un número válido para el índice de la tarea a eliminar.")

    #Funcion para mostrar las tareas
    mostrar_tareas(lista_de_tareas)


if __name__ == "__main__": #Establecemos la función por la que comenzará el programa
    main()
