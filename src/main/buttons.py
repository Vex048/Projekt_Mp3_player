from abc import ABC, abstractmethod
import tkinter as tk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

class button(tk.Button,ABC): # Tworzenie klasy abstrakcyjnej button dziedziczać klasę tk.Button 
    def __init__(self,frame,col,command,fg_color):
        self.color = col
        #self.image=icon
        self.frame=frame
        self.fg_color=fg_color
        self.command=command
        super().__init__(frame) # Wywołoujemy konstruktor dla klasy tk.Button 
        self['border']=0
        self['bg'] = col
        #self['image']=icon
        self['command']=command
        self['state']="disabled"
        self['highlightbackground']=fg_color

      
    @abstractmethod # Abstrackyjna metoda 
    def click_function(self):
        pass 
    
    def setDisabled(self):
        self['state']="disabled"

    def setEnable(self):
        self['state']="normal"

    #Method which will be overriding by polimorhpism
    def resizeImage(self,image):
        # Zmienienie wielkosci ikon odtwarzacza
        image1 =Image.open(image)
        resize_image=image1.resize((35,35))
        button=ImageTk.PhotoImage(resize_image)
        return button
    
    @abstractmethod
    def Images(self):
        pass


class pauseButton(button):
    def __init__(self, frame, col,command,fg_color):
        super().__init__(frame, col,command,fg_color)
        self.Images()
        self['image']=self.download_pause
        self.unclikced_imgae=self.download_play
        self.clicked_image=self.download_pause
        self.buttonState=1
        self.bind("<Button-1>", self.click_function)
    
    
    #overriding abstract method
    def click_function(self,event=None):
        if self['state'] != "disabled":
            self.buttonState = self.buttonState * (-1)
            if self.buttonState == 1:
                self['image']=self.clicked_image
            else:
                self['image']=self.unclikced_imgae



    def Images(self):
        self.download_pause=self.resizeImage('../assets/pause.png')
        self.download_play=self.resizeImage('../assets/play.png')

class loopRandomButton(button):
    def __init__(self, frame, col, command,fg_color):
        super().__init__(frame, col, command,fg_color)
        self.Images()
        self['image']=self.download_random
        self.unclikced_imgae=self.downolad_loop
        self.clicked_image=self.download_random
        self.buttonState=1
        self.bind("<Button-1>", self.click_function)
        self['state']="normal"
    #overriding abstract method
    def click_function(self,event=None):
        if self['state'] != "disabled":
            self.buttonState = self.buttonState * (-1)
            if self.buttonState == 1:
                self['image']=self.clicked_image
            else:
                self['image']=self.unclikced_imgae

    def Images(self):
        self.downolad_loop=self.resizeImage('../assets/loop.png')
        self.download_random=self.resizeImage('../assets/random.png')

class nextButton(button):
    def __init__(self,frame,col,command,fg_color):
        super().__init__(frame, col,command,fg_color) # Wywołany konstruktor klasy z której dziedziczymy 
        self.Images()
        self['image']=self.download_next

    def click_function(self):
        pass

    
    # Method overrdiding
    def resizeImage(self,image):
        # Zmienienie wielkosci ikon odtwarzacza
        image1 =Image.open(image)
        resize_image=image1.resize((30,30))
        button=ImageTk.PhotoImage(resize_image)
        return button
    def Images(self):
        self.download_next=self.resizeImage('../assets/next.png')

class previousButton(button):
    def __init__(self,frame,col,command,fg_color):
        super().__init__(frame, col,command,fg_color)
        self.Images()
        self['image']=self.download_previous
    def click_function(self):
        pass

    
    def resizeImage(self,image):
        # Zmienienie wielkosci ikon odtwarzacza
        image1 =Image.open(image)
        resize_image=image1.resize((30,30))
        button=ImageTk.PhotoImage(resize_image)
        return button
    def Images(self):
        self.download_previous=self.resizeImage('../assets/previous.png')
class stopButton(button):
    def __init__(self,frame,col,command,fg_color):
        super().__init__(frame, col,command,fg_color)
        self.Images()
        self['image']=self.download_stop
    def click_function(self):
        pass


    def Images(self):
          self.download_stop=self.resizeImage('../assets/stop.png')

