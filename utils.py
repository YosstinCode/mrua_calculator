import os

def pedir_datos(*args):

    valores = []

    os.system("cls")

    for variable in args:
        variable = float(input(f"Ingrese el valor de {variable}: "))
        print("")
        valores.append(variable)

    return valores