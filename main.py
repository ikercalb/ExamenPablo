#!/usr/bin/env python3  
import leer
import crear
import actualizar
import borrar

while True:
    modo = input("¿Qué modo deseas: Información de los vuelos, Añadir un vuelo, Modificar un vuelo existente o Borrar un vuelo (informacion, añadir, modificar borrar)? o 'salir' para salir: ").lower()
        
    if modo == "salir":
        print("Saliendo del programa.")
        break  
           
    match modo:
        case "informacion":
            print("Modo 1: Informacion")
            leer.leer()
        case "añadir":
            print("Modo 2: Añadir")
            crear.crear()
        case "modificar":
            print("Modo 3: Modificar")
            actualizar.actualizar()
        case "borrar":
            print("Modo 4: Borrar")
            borrar.borrar()
        case _:
            print("Modo no válido.")
                

