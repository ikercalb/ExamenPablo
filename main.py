#!/usr/bin/env python3  
import re
from datetime import datetime
import json
import os

def cargar_array1():
    with open("datos.json", "r") as archivo:
        try:
            diccionario = json.load(archivo)
        except(json.decoder.JSONDecodeError):
            print("no hay datos")
            diccionario={}
        for d in diccionario:
            p1 = Persona(d.get("dni"),d.get("nombre"),d.get("edad"),d.get("fechaNac"))
            personas.append(p1)
def guardarJson2(personas):
    personas=[p.aDiccionario()for p in personas]
    archivo=open("datos.json","w")
    data=json.dumps(personas)
    archivo.write(data)
    archivo.close
while True:
    modo = input("¿Qué modo deseas: crear, leer, actualizar o borrar(c r u d)? o 's' para salir: ")
        
    if modo == "s":
        break  
        
    match modo:
        case "c":
            print("Modo 1: Crear")
            crear.crear()
        case "r":
            print("Modo 2: Leer")
            leer.leer()
        case "u":
            print("Modo 3: Actualizar")
            actualizar.actualizar()
        case "d":
            print("Modo 4: Borrar")
            borrar.borrar()
                
        case _:
            print("Modo no válido.")
                

