import os
import time
import csv

empleados=[]
promedio_sueldo=["300.000 , 2.500.000"]

def limpiar_pantalla():
    os.system('cls')

def asignar_sueldo():

    try:
        nombre=input("Nonbre y A pellido")
        sueldo=float(input("ingrese el sueldo del empleado"))
        empleados.append({'nombre':nombre},{'sueldo':sueldo})
        print(f"sueldo asignado a{nombre} con exito")
    except ValueError:
        print("error el sueldo debe ser un numero.\n")

def clasificar_sueldo():
    try:
        empleados= sorted(empleados, key= lambda x: x['sueldo'],reserve=True)
        print("empleados clasificados por sueldo")
        print()
    except Exception as e:
        print(f"error al clasificar")


def ver_estadistica():
    try:
        if not empleados:
            print("no hay empleados registrados")
            return
        total_sueldo=sum(emp['sueldo'] )
        for emp in empleados:
            max_sueldo=max(empleados,key=lambda x:x['sueldo'])
            min_sueldo=min (empleados, key=lambda x:x['sueldo'])

            print(f"total de sueldo:${total_sueldo}")
            print(f"promedio de sueldo:${promedio_sueldo}")
            print(f"sueldo maximo:{max_sueldo['nombre']} con $ {max_sueldo['sueldo']}")
            print(f"sueldo maximo:{min_sueldo['nombre']} con $ {min_sueldo['sueldo']}")
    except Exception as e:
            print("error aql obtener la estadistica")

def reporte_sueldo():
    try:
        empleados= f"sueldo_reporte_{time.strftime('%y%m%d-%h%m%s')}.csv"
        with open("empleados","w",newline='')as file:
            fieldnames=['nombre','sueldo']
            writer=csv.DictWriter(file,fieldnames=fieldnames)

            writer.writeheader()
            for emp in empleados:
                for emp in empleados:
                    writer.writerow(emp)
                print(f"reporte de sueldo guardado")
    except Exception as e:
        print(f"error al guardar")

def sumar_sueldo():
    try:
        total_sueldo= sum(emp['sueldo'])
        for emp in empleados:
            print(f"la suma total de los sueldos")
    except Exception as e:
        print(f"error al sumar los sueldos")


def menu():
    empleados=[]
    while True:
        print("1-asignar sueldo")
        print("2- clasificar sueldos")
        print("3- ver estadisticas")
        print("4-reportes de sueldos")
        print("5- salir del programa")

        try:
            opcion=input("ingrese una opcion valido del 1 al 5")
        except ValueError:
            print("ingrese una opcion valida del1 al 5")
            continue
         
        if opcion=='1':
            asignar_sueldo()
        elif opcion=='2':
            clasificar_sueldo()
        elif opcion=='3':
            ver_estadistica()
        elif opcion=='4':
            reporte_sueldo()
        elif opcion=='5':
            print("saliendo del programa:")
            break
        else:
            print("opcion no valida.ingrese una opcion valida del 1 al 5")

if __name__=="__menu__":
    menu()
    