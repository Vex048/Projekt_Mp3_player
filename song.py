from pygame import mixer
class Song:
    is_played=None
    is_paused=None
    def __init__(self,url):
        self.is_played=False
        self.is_paused=False
        self.url=url

    
    def play_song(self):
        mixer.init()
        mixer.music.load(self.url)
        mixer.music.play()
        self.is_played=True

    def check_if_finished(self):
        if mixer.music.get_busy() == True or self.is_paused==True:
            self.is_played=True
        else:
            self.is_played=False  
        
    def input_for_playing_song(self,input):
        match input:
            case "p":
                if self.is_played == True:
                    self.pause_unpause_song()
            case "s":
                if self.is_played == True:
                    self.stop_song()

    def set_volume(self,volumee):
        mixer.music.set_volume(volumee)
        print("Ustawiono wartość dzwięku na:{}".format(volumee))

    def pause_unpause_song(self): 
        if self.is_played==True and self.is_paused==False:
            mixer.music.pause()
            self.is_paused=True
            print("Zpauzowano piosenke")
        elif self.is_played==True and self.is_paused==True:
            mixer.music.unpause()
            self.is_paused=False
            print("Odpauzowano ppiosenke")
     
    
    def stop_song(self):
        self.check_if_finished()
        if self.is_played == True:
            mixer.music.stop()
            self.is_played=False
            print("Przerwano piosenke")
        else:
            print("Nie puszczana jest żadna piosenka")

    def play_next_song(self,current_queue):
        if len(current_queue.songs_queue) == 0:
            return 0
        else:
            next_song_url=current_queue.get_from_queue()
            print(next_song_url)
            self.stop_song()
            new_song=Song(next_song_url)
            new_song.play_song()
            self.is_played=True
            self.is_paused=False
    def queue_song(self,current_queue):
        if len(current_queue.songs_queue) == 0:
            print("nie ma aktualnie piosenki w playliscie")
        else:
            next_song_url=current_queue.get_from_queue()
            mixer.music.queue(next_song_url)
         
              




                


    
        






        


        

    

