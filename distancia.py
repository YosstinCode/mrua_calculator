import os
from utils import pedir_datos

def calcular_distancia_vit():

    datos = pedir_datos("velocidad inicial", "velocidad final", "tiempo")

    # Distancia = (velocidad_i + velocidad_f) * tiempo / 2
    return (datos[0] + datos[1]) * datos[2] / 2


def calcular_distancia_vta():

    datos = pedir_datos("velocidad inicial", "tiempo", "aceleracion")

    # Distancia = (velocidad_i * tiempo) + (0.5 * aceleracion * (tiempo**2))
    return datos[0] * datos[1] + (0.5 * datos[2] * (datos[1]**2))


def calcular_distancia_vfa():

    datos = pedir_datos("velocidad final", "tiempo", "aceleracion")

    # Distancia = (velocidad_f * tiempo) - (0.5 * aceleracion * (tiempo**2))
    return datos[0] * datos[1] - (0.5 * datos[2] * (datos[1]**2))


def calcular_distancia():

    os.system("cls")

    print("Calculadora de distancia\n")
    print("1. Calcular distancia con velocidad inicial, velocidad final y tiempo")
    print("2. Calcular distancia con velocidad inicial, tiempo y aceleracion")
    print("3. Calcular distancia con velocidad final, tiempo y aceleracion\n")

    opcion = int(input("Ingrese la opcion que desea: "))

    opciones = {
        1: calcular_distancia_vit,
        2: calcular_distancia_vta,
        3: calcular_distancia_vfa
    }

    return opciones[opcion]()