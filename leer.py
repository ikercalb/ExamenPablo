#!/usr/bin/env python3
from vuelo import Vuelo

vuelos = []


def leer():
        vuelos = Vuelo.cargar_array()
        if vuelos!= None:
            for v in vuelos:
                print(v)
    

