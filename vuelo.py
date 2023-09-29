#!/usr/bin/env python3import json
import json
vuelos = []


class Vuelo:
    def __init__(self,id_vuelo,destino_vuelo,fecha_vuelo,plazas_vuelo):
        self.id_vuelo=id_vuelo
        self.destino_vuelo=destino_vuelo
        self.fecha_vuelo=fecha_vuelo
        self.plazas_vuelo=plazas_vuelo
    def toDiccionario(self):
        return{
            "id_vuelo":self.vuelo,
            "destino_vuelo":self.destino_vuelo,
            "fecha_vuelo":self.fecha_vuelo,
            "plazas_vuelo":self.plazas_vuelo
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
        personas_dict = [v.to_dict() for v in array_vuelos]
        text_file = open("vuelos.json", "w")
        json_data = json.dumps(personas_dict)
        text_file.write(json_data)
        text_file.close()