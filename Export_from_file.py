import json
import globaly
class Exporter: # Class which is made to read from json 
    def __init__(self):
        pass
    def read_from_json(self):
        with open('D:\PROJEKT_MP3_PLAYER\playlist.json','r') as f:
            data = json.loads(f.read())
        return data

