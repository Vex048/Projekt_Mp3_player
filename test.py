class Piosenka:
    def __init__(self):
        self.__paused=False
        self.__played=False
    
    def set_played(self,temp):
        self.__played=temp
        
    def set_paused(self,temp):
        self.__paused=temp
        

    def get_played(self):
        x=self.__played
        return x

    def get_paused(self):
        x=self.__paused
        return x
song=Piosenka()
song.set_paused(True)
print(song.get_paused())