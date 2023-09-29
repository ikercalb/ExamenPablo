#!/usr/bin/env python3
from vuelo import Vuelo
from vuelo import array_vuelos

def borrar():
    encontrado=False
    Vuelo.cargar_array()
    idV=input("Introduce el id del vuelo que seas borrar:")
    for p in array_vuelos:
        print(p.id_vuelo)
    for p in array_vuelos:
        if p.id_vuelo==idV:
            print("Se borra")
            array_vuelos.remove(p)
            encontrado=True
            Vuelo.cargar_json(array_vuelos)

    if encontrado==False:
        print("No se ha encontrado ningun vuelo con ese id")
    

