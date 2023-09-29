#!/usr/bin/env python3
from vuelo import Vuelo

def actualizar():

    vuelos = Vuelo.cargar_array()
    id_vuelo_a_buscar = input("Introduce el identificador de vuelo a buscar: ")
    vuelo_encontrado = False

    if vuelos != None:
        for vuelo in vuelos:
            if id_vuelo_a_buscar == vuelo.id_vuelo:
                modo = input("¿Qué modo deseas: modificar numero plazas ('p') o destino del vuelo ('d'): ")
                if modo == "p":
                    nuevo_numero_plazas = int(input("Introduce el nuevo número de plazas: "))
                    vuelo.plaza_vuelo = nuevo_numero_plazas
                    print("Número de plazas actualizado.")
                    Vuelo.cargar_json(vuelos)
                    vuelo_encontrado = True
                    break
                elif modo == "d":
                    nuevo_destino = input("Introduce el nuevo destino del vuelo: ")
                    vuelo.destino_vuelo = nuevo_destino
                    print("Destino del vuelo actualizado.")
                    Vuelo.cargar_json(vuelos)
                    vuelo_encontrado = True
                    break
                else:        
                    print("Opcion no valida")
                    vuelo_encontrado = True
                    break
        if not vuelo_encontrado:
            print("No se ha encontrado el vuelo con el indicador:", id_vuelo_a_buscar)
        

   


