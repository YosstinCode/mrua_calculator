import os
from utils import pedir_datos

def calcular_tiempo():

    datos = pedir_datos("velocidad inicial", "velocidad final", "aceleracion")

    # Tiempo = (Velocidad final - Velocidad inicial) / Distancia
    return (datos[1] - datos[0]) / datos[2]
