from abc import ABC, abstractmethod
import tkinter as tk
import song
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

class button(tk.Button,ABC): # Tworzenie klasy abstrakcyjnej button dziedziczać klasę tk.Button 
    def __init__(self,frame,col,icon,command,fg_color):
        self.color = col
        self.image=icon
        self.frame=frame
        self.fg_color=fg_color
        self.command=command
        super().__init__(frame) # Wywołoujemy konstruktor dla klasy tk.Button 
        self['border']=0
        self['bg'] = col
        self['image']=icon
        self['command']=command
        self['state']="disabled"
        self['highlightbackground']=fg_color

        
    @abstractmethod # Abstrackyjna metoda 
    def click_function(self):
        pass 
    

class pauseButton(button):
    def __init__(self, frame, col, icon,command,icon2,fg_color):
        super().__init__(frame, col, icon,command,fg_color)
        self.unclikced_imgae=icon2
        self.clicked_image=icon
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


class loopRandomButton(button):
    def __init__(self, frame, col, icon, command,icon2,fg_color):
        super().__init__(frame, col, icon, command,fg_color)
        self.unclikced_imgae=icon2
        self.clicked_image=icon
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

class nextButton(button):
    def __init__(self,frame,col,icon,command,fg_color):
        super().__init__(frame, col, icon,command,fg_color) # Wywołany konstruktor klasy z której dziedziczymy 
    def click_function(self):
        pass 

class previousButton(button):
    def __init__(self,frame,col,icon,command,fg_color):
        super().__init__(frame, col, icon,command,fg_color)
    def click_function(self):
        pass 
class stopButton(button):
    def __init__(self,frame,col,icon,command,fg_color):
        super().__init__(frame, col, icon,command,fg_color)
    def click_function(self):
        pass     

