import eyed3
import os
import json



class Importer:
    def __init__(self):
        pass
    
    def import_mp3_to_json(self):
        all_songs=[]
        os.chdir('D:\PROJEKT_MP3_PLAYER\SONGS')
        for filename in os.listdir('D:\PROJEKT_MP3_PLAYER\SONGS'):
            f=os.path.join(filename)
            audio=eyed3.load(f)
            # title=audio.tag.title
            # artist=audio.tag.artist
            # mydict = {'title': title, 'author': artist}
            mydict={'title': str(audio)}
            all_songs.append(mydict)
            with open('D:\PROJEKT_MP3_PLAYER\playlist.json','w') as f:
                f.write(json.dumps(all_songs,indent =2))
     


