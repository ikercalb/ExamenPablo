#!/usr/bin/env python3
import json
import time

vuelos = []

class Vuelo:
    
    def __init__(self, id_vuelo, destino_vuelo, fecha_vuelo, plaza_vuelo):
        self.id_vuelo = id_vuelo
        self.destino_vuelo = destino_vuelo
        self.fecha_vuelo = fecha_vuelo
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
            "destino_vuelo": self.destino_vuelo,
            "fecha_vuelo": self.fecha_vuelo,
            "plaza_vuelo": self.plaza_vuelo
        }
        
    def cargar_array():
        vuelos.clear()
        try:
            with open("vuelos.json", "r") as archivo:
                diccionario = json.load(archivo)
                for d in diccionario:
                    v1 = Vuelo(d.get("fecha_vuelo"),d.get("id_vuelo"),d.get("destino_vuelo"),d.get("plaza_vuelo"))
                    vuelos.append(v1)
                return(vuelos)
        except:
            print("No hay vuelos guardados")

    def cargar_json(array_vuelos):
        personas_dict = [v.to_diccionario() for v in array_vuelos]
        text_file = open("vuelos.json", "w")
        json_data = json.dumps(personas_dict)
        text_file.write(json_data)
        text_file.close()