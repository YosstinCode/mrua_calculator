import os
from utils import pedir_datos


def calcular_velocidad_inicial_vfta():

    datos = pedir_datos("velocidad final", "tiempo", "aceleracion")

    # Velocidad inicial = Velocidad final - (Aceleración * Tiempo)
    return datos[0] - (datos[1] * datos[2])


def calcular_velocidad_inicial_vftd():

    datos = pedir_datos("velocidad final", "tiempo", "distancia")

    # Velocidad inicial = (Velocidad final - 2 * Aceleración * Distancia)1/2
    return (datos[0] - 2 * datos[1] * datos[2])**(0.5)


def calcular_velocidad_inicial():
    os.system("cls")

    print("Calculadora de velocidad inicial\n")
    print("1. Calcular velocidad inicial con velocidad final, tiempo y aceleracion")
    print("2. Calcular velocidad inicial con velocidad final, tiempo y distancia\n")

    opcion = int(input("Ingrese la opcion que desea: "))

    opciones = {
        1: calcular_velocidad_inicial_vfta,
        2: calcular_velocidad_inicial_vftd
    }

    return opciones[opcion]()

    # Velocidad inicial = Velocidad final - Aceleración * Tiempo
    # Velocidad inicial = (Velocidad final - 2 * Aceleración * Distancia)1/2