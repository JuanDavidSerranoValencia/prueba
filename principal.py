"""  1. El programa debe tener un menú que permita al usuario seleccionar diferentes opciones:
agregar cita, buscar cita, modificar cita, cancelar cita y salir del programa.
2. Cada cita médica debe tener los siguientes datos: nombre del paciente, fecha de la cita,
hora de la cita y motivo de la consulta.
3. Al agregar una cita, el programa debe solicitar al usuario que ingrese los datos
correspondientes y luego guardar la cita en un archivo JSON.
4. Al buscar una cita, el programa debe solicitar al usuario un criterio de búsqueda (por
ejemplo, nombre del paciente o fecha de la cita) y mostrar todas las citas que coincidan
con ese criterio.
5. Al modificar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y solicitar los nuevos datos para actualizarla en el archivo JSON.
6. Al cancelar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y eliminarla del archivo JSON.
7. Al salir del programa, se deben guardar todos"""

import os 
import cita
flagPrincipal =True
while flagPrincipal:
    print("Menu Cita".center(50,"-"))
    print("1.Agregar Cita\n2.Buscar cita\n3.Modificar Cita\n4.Cancelar Cita\n5.Salir del programa")
    try:
        opc= int(input ("Ingrese la opcion que desea realizar:"))
    except Exception:
        print("\nIngrese valores validos.")
    else:
        if( opc == 1):
            cita.crearCitas()
        elif( opc == 2):
            cita.buscarCitas()
        elif( opc == 3):
            cita.modificarCitas()
        elif( opc == 4):
            cita.eliminarCitas()
        elif( opc == 5):
            flagPrincipal = False 
        else:
            print("Ingrese una opcion valida.")