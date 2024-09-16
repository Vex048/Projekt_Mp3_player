import json
import sys
sys.path.insert(1, "../main")
import globaly
class Exporter: # Class which is made to read from json 
    def __init__(self):
        pass
    def read_from_json(self):
        with open(globaly.jsonfile,'r') as f:
            data = json.loads(f.read())
        return data

