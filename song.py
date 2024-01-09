from pygame import mixer
import time
class Song:
    is_played=None
    is_paused=None
    def __init__(self):
        # atrubuty klasy song, do których można dostac się tylko za pomocą setterów i getterów
        self.__is_played=False 
        self.__is_paused=False
        self.__url=None
    
    def set_url(self,temp):
        self.__url=temp
    def get_url(self):
        x=self.__url
        return x

    def set_played(self,temp):
        if (temp==True or temp==False):
            self.__is_played=temp
        else:
            print("Atrybut piosenki może mieć tylko wartość True or False")
        
    def set_paused(self,temp):
        if (temp==True or temp==False):
            self.__is_paused=temp
        else:
            print("Atrybut piosenki może mieć tylko wartość True or False")
        
    def get_played(self):
        x=self.__is_played
        return x

    def get_paused(self):
        x=self.__is_paused
        return x
    
    def play_song(self):
        mixer.init()
        mixer.music.load(self.get_url())
        mixer.music.play()
        self.set_played(True)



    
              




                


    
        






        


        

    

