from gui import GUI
from controller import Controler
import os
import tkinter as tk
class App:
    
    def __init__(self):
        self.path='D:\PROJEKT_MP3_PLAYER\SONGS'
        self.gui=GUI()
        self.controler=Controler()
        self.bindPlay()
    
    def bindPlay(self):
        self.gui.songName.config(text="jd")
        self.gui.Listbox.bind("<Double-1>",self.activateFromGui)
        print("Zbidnowano")
    def activateFromGui(self):
        print("jd")
        songName=self.gui.activateSong()
        print(songName)
        self.controler.song.url='D:\PROJEKT_MP3_PLAYER\SONGS\{}'.format(songName)
        self.controler.playSong()
        


app=App()