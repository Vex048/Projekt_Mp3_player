import os
import Export_from_file
import random
class Queue:
    songs_queue=[]
    def __init__(self):
        self.songs_queue=[]

    def get_song_to_queue(self,song):
        if song not in self.songs_queue:
            self.songs_queue.append(song)

    def play_from_queue(self):
        current_song=self.songs_queue[0]
        self.songs_queue.pop(0)
        return current_song
    def create_queue_from_file(self):
        #os.chdir('C:\PROJEKT_Mp3Player\SONGS')
        export=Export_from_file.Exporter()
        json_list=export.read_from_json()
        number_of_songs_to_queue=len(json_list)
        list_of_randomly_songs=random.sample(json_list,number_of_songs_to_queue)
        return list_of_randomly_songs

    def fill_up_queue(self,current_song):
        list_of_randomly_songs=self.create_queue_from_file()
        for music in list_of_randomly_songs:
            if music['title'] == current_song:
                continue
            else:
                url='D:\PROJEKT_Mp3_Player\SONGS\{}'.format(music['title'])
                self.get_song_to_queue(url)



queue=Queue()
queue.create_queue_from_file()
queue.fill_up_queue("Warriors.mp3")
print(queue.songs_queue)
print(queue.play_from_queue())