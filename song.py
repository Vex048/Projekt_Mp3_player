from pygame import mixer
import time
class Song:
    is_played=None
    is_paused=None
    def __init__(self,url):
        self.__is_played=False
        self.__is_paused=False
        self.url=url
        
    def set_played(self,temp):
        self.__is_played=temp
        
    def set_paused(self,temp):
        self.__is_paused=temp
        
    def get_played(self):
        x=self.__is_played
        return x

    def get_paused(self):
        x=self.__is_paused
        return x
    
    def play_song(self):
        mixer.init()
        mixer.music.load(self.url)
        mixer.music.play()
        self.set_played(True)
        #self.is_played=True

    def check_if_finished(self):
        # if mixer.music.get_busy() == True or self.is_paused==True:
        #     self.is_played=True
        # else:
        #     self.is_played=False
        temp=self.get_paused()
        if mixer.music.get_busy() == True or temp==True:
            self.set_played(True)
        else:
            self.set_played(False)
        
        

    def set_volume(self,volumee):
        mixer.music.set_volume(volumee)
        print("Ustawiono wartość dzwięku na:{}".format(volumee))

    def pause_unpause_song(self):
        temp1=self.get_played()
        temp2=self.get_paused()
        if temp1==True and temp2==False:
            mixer.music.pause()
            #self.is_paused=True
            self.set_paused(True)
            print("Zpauzowano piosenke")
        elif temp1==True and temp2==True:
            mixer.music.unpause()
            time.sleep(1)
            self.set_paused(False)
            
            print("Odpauzowano ppiosenke")
        
     

    def stop_song(self):
        self.check_if_finished()
        # if self.is_played == True:
        #     mixer.music.stop()
        #     self.is_played=False
        temp=self.get_played()
        if temp == True:
            mixer.music.stop()
            self.set_played(False)
        


    def play_next_song(self,current_queue):
        if len(current_queue.songs_queue) == 0:
            return 0
        else:
            next_song_url=current_queue.get_from_queue()
            print(next_song_url)
            #self.is_played=False
            self.set_played(False)
            time.sleep(0.5)
            self.stop_song()
            
            new_song=Song(next_song_url)
            new_song.play_song()
            # self.is_played=True
            # self.is_paused=False
            self.set_played(True)
            self.set_paused(False)
            

    def queue_song(self,current_queue):
        if len(current_queue.songs_queue) == 0:
            print("nie ma aktualnie piosenki w playliscie")
        else:
            next_song_url=current_queue.get_from_queue()
            mixer.music.queue(next_song_url)

    def check_if_song_finished(self):
        temp1=self.get_played()
        temp2=self.get_paused()
        # if mixer.music.get_busy() == False and self.is_played==True and self.is_paused==False:
        #     return True
        # else:
        #     return False
        if mixer.music.get_busy() == False and temp1==True and temp2==False:
            return True
        else:
            return False
        
    
              




                


    
        






        


        

    

