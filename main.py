import os
from aceleracion import calcular_aceleracion
from distancia import calcular_distancia
from velocidad_final import calcular_velocidad_final
from velocidad_inicial import calcular_velocidad_inicial
from tiempo import calcular_tiempo

def main():

    while True:

        os.system("cls")
        print("Calculadora MRUA\n")
        print("1. Calcular distancia")
        print("2. Calcular velocidad inicial")
        print("3. Calcular velocidad final")
        print("4. Calcular tiempo")
        print("5. Calcular aceleracion")
        print("6. Salir\n")

        opcion = int(input("Ingrese la opcion que desea: "))

        if opcion == 6:
            break;

        opciones = {
            1: ["La distancia es:", calcular_distancia, "m"],
            2: ["La velocidad inicial es:",calcular_velocidad_inicial, "m/s"],
            3: ["La velocidad final es:",calcular_velocidad_final, "m/s"],
            4: ["El tiempo es:", calcular_tiempo, "s"],
            5: ["La aceleracion es:",calcular_aceleracion, "m/s²"]
        }

        os.system("cls")
        
        print(opciones[opcion][0], opciones[opcion][1](), opciones[opcion][2])

        input("\nPresione enter para continuar...")

if __name__ == "__main__":
    main()



