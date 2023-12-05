import tkinter as tk
import song


class button:
    def __init__(self):
        self.is_clicked=False
        self.button=None
        self.__enabled=False
    # def createButton(self):
    #     button = tk.Button(root,text="Pause",width=25,command=root.destroy)
    #     self.button=button
    def set_enabled(self,temp):
        self.__enabled=temp
    def get_enabled(self):
        x=self.__enabled
        return x 

    
class playButton(button):
    pass

class nextButton(button):
    def nextSong(self,current_song,queue):
        temp=self.get_enabled()
        if temp == True:
            current_song.play_next_song(queue)
            print("DZiała z guzika")
        else:
            print("Nie ma żadnej piosneki")


class volumeButton(button):
    def __init__(self):
        self.set_enabled(True)
    pass
class stopButton(button):
    def stop(self,current_song):
        temp=self.get_enabled()
        if temp == True:
            current_song.stop_song()
            print("DZiała z guzika")
        else:
            print("Nie ma żadnej piosneki")
    
    
class pauseButton(button):
    def pauseUnpause(self,current_song):
        temp=self.get_enabled()
        if temp == True:
            current_song.pause_unpause_song()
            print("DZiała z guzika")
        else:
            print("Nie ma żadnej piosneki")
    





# play_Button.button.pack()
# root.mainloop()


    