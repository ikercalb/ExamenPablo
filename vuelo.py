#!/usr/bin/env python3
import json
import time


array_vuelos = []


class Vuelo:
    
    def __init__(self, id_vuelo, destino_vuelo, fecha_vuelo, plaza_vuelo):
        self.id_vuelo = id_vuelo

        self.fecha_vuelo = fecha_vuelo
        
        self.destino_vuelo = destino_vuelo  

        self.plaza_vuelo = plaza_vuelo

    def crear_vuelo(destino_vuelo, fecha_vuelo, plaza_vuelo):
        id_vuelo = Vuelo.generar_id_vuelo()
        vuelo = Vuelo(id_vuelo, destino_vuelo, fecha_vuelo, plaza_vuelo)
        return vuelo

    def generar_id_vuelo():  
        current_time = int(time.time())
        return f"Vuelo_{current_time}"
        
    def to_diccionario(self):
        return {
            "id_vuelo": self.id_vuelo,

            "fecha_vuelo": self.fecha_vuelo,
            "destino_vuelo": self.destino_vuelo,
            

            "plaza_vuelo": self.plaza_vuelo
        }
        
    def cargar_array():

        array_vuelos.clear()

        try:
            with open("vuelos.json", "r") as archivo:
                diccionario = json.load(archivo)
                for d in diccionario:

                    v1 = Vuelo(d.get("id_vuelo"),d.get("fecha_vuelo"),d.get("destino_vuelo"),d.get("plaza_vuelo"))
                    array_vuelos.append(v1)
                return(array_vuelos)


        except:
            print("No hay vuelos guardados")

    def cargar_json(array_vuelos):

        vuelos_dict = [v.to_dict() for v in array_vuelos]
        text_file = open("vuelos.json", "w")
        json_data = json.dumps(vuelos_dict)

        text_file.write(json_data)
        text_file.close()