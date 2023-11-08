from pygame import mixer

class Song:
    is_played=None
    def __init__(self,url):
        self.is_played=False
        self.url=url

    
    def play_song(self):
        mixer.init()
        mixer.music.load(self.url)
        mixer.music.play()
        self.is_played=True

    def check_if_finished(self):
        if mixer.music.get_busy():
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
        if self.is_played==True:
            mixer.music.pause()
            self.is_played=False
            print("Zpauzowano piosenke")
        elif self.is_played==False:
            mixer.music.unpause()
            self.is_played=True
            print("Odpauzowano ppiosenke")

    def is_playing(self):
        if self.is_played == True:
            return True
        else:
            return False
        
    
    def stop_song(self):
        self.check_if_finished()
        if self.is_played == True:
            mixer.music.stop()
            self.is_played=False
            print("Przerwano piosenke")
        else:
            print("Nie puszczana jest żadna piosenka")

        

    
        






        


        

    

