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
from datetime import datetime

dicCitas ={"citas":[]}
fechaLocal=datetime.now()

def crearCitas():
    try:
        
        cita= {
            "nombrePaciente":input("Ingrese el nombre del paciente:").upper(),
            #"fechaCita":datetime.strptime(input("Ingrese la fecha de la cita (yy-mm-dd):"),'%Y-%m-%d'),
            #"horaCita":input("Ingrese la hora de la cita (hh:mm:ss):"),
            "motivo":input("Ingrese el motivo de su consulta:"),
        }
        
    except Exception:
        print("Ingrese valores validos")
    else:
        """if cita["fechaCita"]< fechaLocal:
            print("Verifique sus datos , la fecha debe ser mayor a la del dia de hoy")
        else:"""
        dicCitas['citas'].append(cita)
        print("Cita añadida con exito".center(50))
        
def buscarCitas():
    nombre= input("Ingrese la cedula del paciente para verificar las cita vigentes:").upper()
    lista= []
    for i , item in enumerate(dicCitas["citas"]):
        if nombre==item["nombrePaciente"]:
            lista.append(item)
    if len(lista)>0:
        for i, item in enumerate(lista):
            print(f"{i}-{item}")
    else:
        print("la cedula del paciente no se encuentra registrada")
        
def modificarCitas():
    nombre = input("Ingrese el nombre del paciente:").upper()
    lista =[]
    for i , item in enumerate(dicCitas["citas"]):
        if nombre==item["nombrePaciente"]:
            lista.append(item)
    if len(lista)>0:
        for i , item in enumerate(lista):
            print(f"{i+1}.{item}")
        cita= lista[int(input("Seleccione la cita que desea actualizar"))-1]
        cita['motivo']=input("Ingrese un nuevo motivo o presione enter para omitir:") or cita['motivo']
        print("cita actualizada con exito.")
        
    else:
        print("la cedula del paciente no se encuentra registrada")
            
        
def cancelarCitas():
    nombre = input ("ingrese el nombre del paciente al que desea eliminar una cita:").upper()
    lista=[]
    for i , item in enumerate (dicCitas["citas"]):
        if nombre == item ["nombrePaciente"]:
            lista.append(item )
    if (len(lista)>0):
        for i , item in enumerate (lista):
            print(f"{i+1} - {item}")
        dicCitas["citas"].remove(lista[int(input("Ingrese la cita que desea eliminar:"))-1])
        print("Cita eliminada con exito.")    
    else:
        print("El nombre ingresado no tiene citas registradas.")
      

