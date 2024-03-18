import eyed3
import os
import json
import globaly


class Importer: # Klasa dzięki, której zapisujemy pliki mp3 z folderu jsona, który służy jako referancja do plików mp3
    def __init__(self):
        pass
    
    def import_mp3_to_json(self):
        eyed3.log.setLevel("ERROR")
        all_songs=[]
        os.chdir(globaly.activeDirectory)
        for filename in os.listdir(globaly.activeDirectory):
            f=os.path.join(filename)
            audio=eyed3.load(f)
            mydict={'title': str(audio)}
            all_songs.append(mydict)
            with open(globaly.jsonfile,'w') as f:
                f.write(json.dumps(all_songs,indent =2))
     


