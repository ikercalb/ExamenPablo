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
  