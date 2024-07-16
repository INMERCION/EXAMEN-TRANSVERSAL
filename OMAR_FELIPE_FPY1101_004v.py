import csv
import random
import math


trabajadores = [
    {"nombre":"Juan Pérez      ","sueldo":0},
    {"nombre":"María García    ","sueldo":0},
    {"nombre":"Carlos López    ","sueldo":0},
    {"nombre":"Ana Martínez    ","sueldo":0},
    {"nombre":"Pedro Rodríguez ","sueldo":0},
    {"nombre":"Laura Hernández ","sueldo":0},
    {"nombre":"Miguel Sánchez  ","sueldo":0},
    {"nombre":"Isabel Gómez    ","sueldo":0},
    {"nombre":"Francisco Díaz  ","sueldo":0},
    {"nombre":"Elena Fernández ","sueldo":0}
    ]

def menu():
        
    while True:
        print("""\n\tDuoc UC 
    1.	Asignar sueldos aleatorios
    2.	Clasificar sueldos
    3.	Ver estadísticas
    4.	Generar reporte de sueldos
    5.	Salir del programa

            """)
        opc=input("\tOPC: ")
        if opc=="1":
            asignar()

        elif opc=="2":
            clasificar()

        elif opc=="3":
            estadisticas()

        elif opc=="4":
            reporte()

        elif opc=="5":
            print("\nFinalizando Programa.....")
            print("Desarrollado por Omar Felipe")
            print("RUT: 25.938.685-3\n")
            break
            
        else:
            print("\nElija una opcion correcta")    

def asignar():

    print("\nNOMBRE:\t\t   SUELDO:")
    for trabajador in trabajadores:
        trabajador["sueldo"]=random.randint(300000, 2500000)
        print(f"{trabajador["nombre"]} $ {trabajador["sueldo"]}")

def clasificar():
    bajo=[]
    medio=[]
    alto=[]

    for trabajador in trabajadores:
        if trabajador["sueldo"]<800000:
            bajo.append(trabajador)
        elif 800000<=trabajador["sueldo"]<2000000:
            medio.append(trabajador)
        elif trabajador["sueldo"]>=2000000:
            alto.append(trabajador)

    print("\nClasificacion de Sueldos:")
    print(f"\nSUELDOS INFERIORES A $ 800.000, TOTAL: {len(bajo)}")
    print("\nNOMBRE:\t\t   SUELDO:")
    for trabajador in bajo:
        print(f"{trabajador["nombre"]} $ {trabajador["sueldo"]}")

    print(f"\nSUELDOS ENTRE $ 800.000 - $ 2.000.000, TOTAL: {len(medio)}")
    print("\nNOMBRE:\t\t   SUELDO:")
    for trabajador in medio:
        print(f"{trabajador["nombre"]} $ {trabajador["sueldo"]}")
        
    print(f"\nSUELDOS SUPERIORES A $ 2.000.000, TOTAL: {len(alto)}")
    print("\nNOMBRE:\t\t   SUELDO:")
    for trabajador in alto:
        print(f"{trabajador["nombre"]} $ {trabajador["sueldo"]}")

def estadisticas():
    print("\nEstadisticas de la Empresa:")
    sueldos=[trabajador["sueldo"] for trabajador in trabajadores ]
    print(f"\nSueldo más alto     :$ {min(sueldos)}")
    print(f"Sueldo más bajo     :$ {max(sueldos)}")
    print(f"Promedio de sueldos :$ {sum(sueldos)/len(sueldos)}")
    print(f"Media geométrica    :$ {math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos)):.2f}")

def reporte():
   
   with open("reporte.csv", "w" , newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["nombre","sueldo base","Desc. Salud","Desc. AFP","sueldo liquido"])
    
    print("\nNombre:\t\tSueldo Base:\tDesc. Salud:\tDesc. AFP:\tSueldo Líquido:")
    for trabajador in trabajadores:
        sueldo = trabajador["sueldo"]
        descuento_salud = round(sueldo * 0.07)
        descuento_afp = round(sueldo * 0.12)
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        writer.writerow([trabajador["nombre"], sueldo, descuento_salud, descuento_afp, sueldo_liquido])
        print(f"{trabajador['nombre']} $ {sueldo}\t $ {descuento_salud}\t $ {descuento_afp} \t $ {sueldo_liquido}")

    print("\nSe ha generado el reporte de sueldos en 'reporte.csv'")

if __name__=="__main__":
    menu()