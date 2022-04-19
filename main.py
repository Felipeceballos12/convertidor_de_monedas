import os
import time

from menu import menu_programa
from convertir_usd_a_cop import convertir_usd_a_cop
from convertir_cop_a_usd import convertir_cop_a_usd

operacion_elegida = ""

while operacion_elegida.lower() != "s":

    os.system("clear")
    operacion_elegida = menu_programa()

    if operacion_elegida == "1":

        print("\n============= Convertir USD a COP =============\n")

        valor_ingresado = input("Cuantos dolares tienes? ")
        convertir_usd_a_cop(valor_ingresado)

        time.sleep(5)

    elif operacion_elegida == "2":

        print("\n============= Convertir COP a USD =============\n")

        valor_ingresado = input("Cuantos pesos colombianos tienes? ")
        convertir_cop_a_usd(valor_ingresado)

        time.sleep(5)
