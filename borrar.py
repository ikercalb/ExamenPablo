#!/usr/bin/env python3
from vuelo import Vuelo
from vuelo import vuelos

def borrar():
    encontrado=False
    Vuelo.cargar_array
    idV=input("Introduce el id del vuelo que seas borrar:")
    for p in vuelos:
        if p.id_vuelo==idV:
            vuelos.remove(p)
            encontrado=True
    if encontrado==False:
        print("No se ha encontrado ningun vuelo con ese id")
    Vuelo.cargar_json


