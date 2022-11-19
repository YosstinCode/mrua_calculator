import os
from utils import pedir_datos


def calcular_velocidad_final_vita():

    datos = pedir_datos("velocidad inicial", "tiempo", "aceleracion")

    # Velocidad final = Velocidad inicial + Aceleración * Tiempo
    return datos[0] + (datos[1] * datos[2])


def calcular_velocidad_final_vitd():

    datos = pedir_datos("velocidad inicial", "tiempo", "distancia")

    # Velocidad final = (Velocidad inicial + 2 * Aceleración * Distancia)1/2
    return (datos[0] + 2 * datos[1] * datos[2])**(0.5)


def calcular_velocidad_final():

    os.system("cls")
    print("Calculadora de velocidad final\n")
    print("1. Calcular velocidad final con velocidad inicial, tiempo y aceleracion")
    print("2. Calcular velocidad final con velocidad inicial, tiempo y distancia\n")

    opcion = int(input("Ingrese la opcion que desea: "))

    opciones = {
        1: calcular_velocidad_final_vita,
        2: calcular_velocidad_final_vitd
    }

    return opciones[opcion]()

    # Velocidad final = Velocidad inicial + Aceleración * Tiempo
    # Velocidad final = (Velocidad inicial + 2 * Aceleración * Distancia)1/2