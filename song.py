from pygame import mixer
import queue_1
class Song:
    is_played=None
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

        def play_next_song(self):
            if queue_1.queue.songs_queue == []:
                return "Nie ma żadnej muzyki w kolejce"
            else:
                next_song=queue_1.queue.play_from_queue()
                if self.check_if_finished() == True:
                    self.play_song(next_song)


    
        






        


        

    

