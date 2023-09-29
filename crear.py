#!/usr/bin/env python3
from vuelo import Vuelo
from datetime import datetime

vuelos = []

def leerFechaValida():
    
    while True:
        try:
            fecha=input("Introduce una fecha YYYY-MM-DD: ")
            fecha=datetime.strptime(fecha,'%Y-%m-%d')
            return fecha.timestamp()
        except ValueError:
            print("Error, formato de fecha incorrecto")

def crear():
    vuelos = Vuelo.cargar_array()
    
    fech = leerFechaValida()
    
    des = input("Introduce el destino: ").lower()
    
    pla = input("Introduce las plazas libres: ")
    while True:
        if pla.isnumeric():
            break
        else:
            pla = input("Introduce un valor correcto para las plazas libres: ")
            
    v1 = Vuelo.crear_vuelo(des, fech, pla)
    if vuelos != None:
        vuelos.append(v1)
    else:
        vuelos=[v1] 
        
    Vuelo.cargar_json(vuelos)




