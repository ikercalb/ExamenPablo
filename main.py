#!/usr/bin/env python3  
import re
from datetime import datetime
from vuelo import Vuelo
from vuelo import array_vuelos
import borrar
import json
import os


archivoJson = "vuelos.json"

# Comprueba si el archivo JSON ya existe
if not os.path.exists(archivoJson):
    # El archivo no existe, así que lo creamos
    with open(archivoJson, "w") as nuevo_archivo_json:
        # No escribimos ningún contenido en el archivo en este caso
        pass
    print("Archivo JSON creado. No hay datos.")
else:
    print("El archivo JSON ya existe, no se realizó ninguna escritura.")


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
                

