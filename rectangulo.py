import numpy as np

class rectangulo:

    def __init__(self):
        self.principal()

    def principal(self):
        # -*- coding: utf-8 -*-
        # Decoración: Nombre del Algoritmo - Falta decoración que maneja el formato de los menus anteriores
        # Entradas
        print("Ingrese Base y Alto: ")
        BASE = float(input("Base: "))
        ALTO = float(input("Alto: "))

        SUP = BASE * ALTO
        PER = 2 * (BASE + ALTO)
        # Salida
        print("\nSALIDA: ")
        print("-------------------------------------------------------")
        print("Superficie:", SUP)
        print("Perímetro:", PER)