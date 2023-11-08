import os
import json
class Queue:
    list_songs=[]
    def __init__(self):
        self.list_songs=[]
        

    def get_song(self,song):
        self.list_songs.append(song)

    def check_if_queue_empty(self):
        if len(self.list_songs) == 0:
            return  
