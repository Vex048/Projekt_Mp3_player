import os
import Export_from_file
import random
import globaly
class Queue:
    songs_queue_random=[]
    def __init__(self):
        #Konstruktor, który tworzy kolejki dla różnych stateow przycisku LoopRandom 
        self.songs_queue_random=[]
        self.previousQueue_random=[]
        self.songs_queue_loop=[]

    def get_song_to_queue(self,song): # Wrzucenie piosenki do kolejki
        if song not in self.songs_queue_random:
            self.songs_queue_random.append(song)
    
    def get_song_to_queue_loop(self,song):
        if song not in self.songs_queue_loop:
            self.songs_queue_loop.append(song)

    def getSongPreviousQueue(self,song):
        if song not in self.previousQueue_random:
            self.previousQueue_random.append(song)


    def check_for_songs_queue(self,current_song): # Sprawdzanie czy kolejki nie są puste
        if self.songs_queue_random == []:
            self.fill_up_queue_random(current_song)
        if self.songs_queue_loop == []:
            self.fill_up_queue_loop(current_song)




    def get_from_queue_random(self): # Getting first song in queue
        current_song=self.songs_queue_random[0]
        self.songs_queue_random.pop(0)
        return current_song
    
    def get_from_queue_loop(self):
        current_song=self.songs_queue_loop[0]
        self.songs_queue_loop.pop(0)
        return current_song
    

    def create_queue_from_file(self): # Creating queue through json and returning two list 
        export=Export_from_file.Exporter()
        json_list=export.read_from_json()
        number_of_songs_to_queue=len(json_list)
        list_of_randomly_songs=random.sample(json_list,number_of_songs_to_queue)
        list_of_randomly_songs2=random.sample(json_list,number_of_songs_to_queue)
        return list_of_randomly_songs, list_of_randomly_songs2
    
    def create_queue_from_file_loop(self): 
        export=Export_from_file.Exporter()
        json_list=export.read_from_json()
        number_of_songs_to_queue=len(json_list)
        list_of_looped_songs=json_list
        list_of_looped_songs2=random.sample(json_list,number_of_songs_to_queue)
        return list_of_looped_songs, list_of_looped_songs2

    def fill_up_queue_random(self,current_song): # Filling up queue 
        list_of_randomly_songs,list_of_randomly_songs2=self.create_queue_from_file()
        tempList=[]
        temp=current_song.get_url()
        nameSong=""
        for s in reversed(temp):
            if s != "/":
                tempList.insert(0,s)
            else:
                break
        nameSong=nameSong.join(tempList)

        for music in list_of_randomly_songs:

            if music['title'] == nameSong:
                continue
            else:
                url='{}/{}'.format(globaly.activeDirectory,music['title'])
                self.get_song_to_queue(url)

        for music in list_of_randomly_songs2:
            if music['title'] == current_song:
                continue
            else:
                url='{}/{}'.format(globaly.activeDirectory,music['title'])
                self.getSongPreviousQueue(url)
    
    def fill_up_queue_loop(self,current_song):
        list_of_looped_songs,list_of_randomly_songs2=self.create_queue_from_file_loop()
        i=0
        j=0
        tempList=[]
        temp=current_song.get_url()
        nameSong=""
        for s in reversed(temp):
            if s != "/":
                tempList.insert(0,s)
            else:
                break
        nameSong=nameSong.join(tempList)

        for music in list_of_looped_songs:

            if music['title'] == nameSong:
                i=1
                continue
            if i==1:
                url='{}/{}'.format(globaly.activeDirectory,music['title'])
                self.get_song_to_queue_loop(url)
            else:
                j=j+1
        for music in list_of_looped_songs:
            if j>0:
                url='{}/{}'.format(globaly.activeDirectory,music['title'])
                self.get_song_to_queue_loop(url)
                j=j-1
            else:
                break
        #Time for previous queue

        for music in list_of_randomly_songs2:
            if music['title'] == current_song:
                continue
            else:
                #url='D:\PROJEKT_Mp3_Player\SONGS\{}'.format(music['title'])
                url='{}/{}'.format(globaly.activeDirectory,music['title'])
                self.getSongPreviousQueue(url)
    
        



