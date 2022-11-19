import os
from utils import pedir_datos

def calcular_aceleracion_vivft():

    datos = pedir_datos("velocidad inicial", "velocidad final", "tiempo")

    # Aceleración = (Velocidad final - Velocidad inicial) / Tiempo
    return (datos[1] - datos[0]) / datos[2]


def calcular_aceleracion_vivfd():

    datos = pedir_datos("velocidad inicial", "velocidad final", "distancia")

    # Aceleración = (Velocidad final - Velocidad inicial) / (2 * Distancia)
    return (datos[1]**2 - datos[0]**2) / (2 * datos[2])


def calcular_aceleracion_vitd():

    datos = pedir_datos("velocidad inicial", "tiempo", "distancia")

    # Aceleración = (Distancia - (Velocidad inicial * Tiempo) ) / (0,5 * Tiempo**2)
    return (datos[2] - (datos[0] * datos[1])) / (0.5 * datos[1]**2)


def calcular_aceleracion_vftd():

    datos = pedir_datos("velocidad final", "tiempo", "distancia")

    # Aceleración = (Distancia + (Velocidad final * Tiempo) ) / (0,5 * Tiempo**2)
    return (datos[2] + (datos[0] * datos[1])) / (0.5 * datos[1]**2)


def calcular_aceleracion():

    os.system("cls")
    print("Calculadora de aceleracion\n")
    print("1. Calcular aceleracion con velocidad inicial, velocidad final y tiempo")
    print("2. Calcular aceleracion con velocidad inicial, velocidad final y distancia")
    print("3. Calcular aceleracion con velocidad inicial, tiempo y distancia")
    print("4. Calcular aceleracion con velocidad final, tiempo y distancia\n")

    opcion = int(input("Ingrese la opcion que desea: "))

    opciones = {
        1: calcular_aceleracion_vivft,
        2: calcular_aceleracion_vivfd,
        3: calcular_aceleracion_vitd,
        4: calcular_aceleracion_vftd
    }

    return opciones[opcion]()