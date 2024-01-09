import tkinter as tk #Biblioteka do tworzenia GUI
import customtkinter #Biblioteka do tworzenia customowego GUI
import buttons #Importowane główne przyciski do sterowania muzyką 
from tkinter import filedialog #Biblioteka do przgeladania plikow
from music_from_yt import downloader_from_youtube # Importowana klasa do pobierania muzyki z yt
from PIL import Image, ImageTk #Importowany moduł do przeróbki Zdjęć 
import os 
from controller import Controler #Importowanie klasy Controllera 
import threading 
import time
import globaly
class GUI:
    def __init__(self):
        self.activeDirectory=globaly.activeDirectory
        self.active=True
        self.controler=Controler()
        self.downolader=downloader_from_youtube()
        x=self.startThread(self.get_function_thread) #Ten wątek sprawdza czy muzyka się skończyła i czy można puścić następną
        x.start()
                # Tworzenia GUI 
        self.root=customtkinter.CTk()   
        self.root.title('MP3 player')
        self.root.protocol("WM_DELETE_WINDOW",self.closing) #Zamykanie programnu na przycisk X lub Wyjdz
        self.initializeGui() #Inicjalizowanie GUI

    def closing(self):
        self.active=False
        self.root.destroy()
    def startThread(self,function):
        t1=threading.Thread(target=function)
        return t1

    def get_function_thread(self):
        while self.active==True:
            time.sleep(0.1)
            if self.controler.check_if_song_finished() == True:
                self.buttonNextAction()

    def initializeGui(self):
        # Inicjalizacja Wszystkich części GUI
        self.Images()
        self.setRootParameters()
        self.setinngFrames()
        self.settingButtons()
        self.settingLabels()
        self.mainMenu.tkraise()
        self.creatingListBox()
        self.creatingRootButtons()
        self.root.mainloop()

    def setRootParameters(self):
        # Ustawianie długości, szerokosci itd.
        self.root.geometry('1000x600')
        self.root.resizable(0,0)
        self.rootHeight=self.root.winfo_height()
        self.rootWidth=self.root.winfo_width()
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0,weight=1)
        
    def setinngFrames(self):
        # Twowrzenie Frameów, które po wciśnięciu odpowiednich przycisków nakładają się na siebie 
        self.mainMenu = customtkinter.CTkFrame(master=self.root,height=self.rootHeight-200,width=self.rootWidth-100)
        self.addSongFrame= customtkinter.CTkFrame(master=self.root,height=self.rootHeight-200,width=self.rootWidth-100)
        self.listSongFrame= customtkinter.CTkFrame(master=self.root,height=self.rootHeight-200,width=self.rootWidth-100)
        for frame in (self.mainMenu, self.addSongFrame, self.listSongFrame):
            frame.grid(row=0, column=0, sticky='news',pady=(0,100))
    
    def getSongUrl(self):
        # Getter URL do piosenki, którą chcemy pobrac z Yt
        url=self.entryUrl.get()
        self.entryUrl.delete(0, tk.END)
        return url

    def setDestroy(self):   
        # Do Zamknięcia aplickacji oraz wątku, który cały czas pracuje w tle
        self.active=False
        self.root.destroy()
    def settingButtons(self):
        #Tworzenie przycisków, dzięki którym poruszamy się po frameach
        customtkinter.CTkLabel(master=self.mainMenu, text='GŁÓWNE MENU').pack(side='top',pady=5)
        customtkinter.CTkButton(master=self.mainMenu, text='Przeładuj pliki',command=self.controler.reloadJson).pack(side='top',pady=5)
        customtkinter.CTkButton(master=self.mainMenu,text='Wylistuj piosenki',command=lambda:self.listSongFrame.tkraise()).pack(side='top',pady=5)
        customtkinter.CTkButton(master=self.mainMenu,text='Dodaj piosenki',command=lambda:self.addSongFrame.tkraise()).pack(side='top',pady=5)
        customtkinter.CTkButton(master=self.mainMenu,text='Wyjdz',command=lambda:self.setDestroy()).pack(side='top',pady=5)

        

    def creatingRootButtons(self):
        # Tworzenie wszystkich przycisków dotyczących sterowaniem odtwarzaczem
        self.Pause_unpause=buttons.pauseButton(self.root,'gray',self.download_pause,self.buttonPauseAction,self.download_play,"white")
        self.Next=buttons.nextButton(self.root,'gray',self.download_next,self.buttonNextAction,"white")
        self.Previous=buttons.previousButton(self.root,'gray',self.download_previous,self.buttonPreviousAction,"white")
        self.Stop=buttons.stopButton(self.root,'gray',self.download_stop,self.buttonStopAction,"white")
        self.volumeScale=customtkinter.CTkSlider(master=self.root,variable=tk.DoubleVar(),from_=1,to=100,orientation='horizontal',command=self.setVolume)#,number_of_steps=0.01)
        self.volumeScale.set(10)
        self.LoopRandom=buttons.loopRandomButton(self.root,'gray',self.download_random,self.buttonLoopRandomAction,self.downolad_loop,"white")
        self.Pause_unpause.place(x=485,y=550)
        self.Next.place(x=535,y=550)
        self.Previous.place(x=435,y=550)
        self.Stop.place(x=350,y=550)
        self.volumeScale.place(x=100,y=550)
        self.LoopRandom.place(x=600,y=550)

    def settingLabels(self):
        #Ustawianie Tesktu i przycisków, aby pasowały
        customtkinter.CTkLabel(master=self.addSongFrame, text='Wpisz url piosenki, która chcesz dodać').pack()
        self.entryUrl= customtkinter.CTkEntry(master=self.addSongFrame,width=400)
        self.entryUrl.pack()
        customtkinter.CTkButton(master=self.addSongFrame,text="Sumbit song",command=self.addSong).pack(pady=5)
        customtkinter.CTkButton(master=self.addSongFrame, text='Powrót', command=lambda:self.mainMenu.tkraise()).pack()
        #customtkinter.CTkLabel(master=self.listSongFrame, text='Tuaj są wylistowane piosenki').pack()
        

    def resizeImage(self,image):
        # Zmienienie wielkosci ikon odtwarzacza
        image1 =Image.open(image)
        resize_image=image1.resize((35,35))
        button=ImageTk.PhotoImage(resize_image)
        return button
    def Images(self):
        #Ikony odtwarzacza
        self.download_pause=self.resizeImage('./assets/pause.png')
        self.download_next=self.resizeImage('./assets/next.png')
        self.download_previous=self.resizeImage('./assets/previous.png')
        self.download_stop=self.resizeImage('./assets/stop.png')
        self.download_play=self.resizeImage('./assets/play.png')
        self.downolad_loop=self.resizeImage('./assets/loop.png')
        self.download_random=self.resizeImage('./assets/random.png')

    def creatingListBox(self):
        # Tworzenie Listboxu, dzięki któremu możemy odpalić daną piosenkę
        self.Listbox=tk.Listbox(self.listSongFrame,width=100,height=20)
        self.creatingSongForListbox()
        self.Listbox.pack()
 
        self.songName=customtkinter.CTkLabel(master=self.root,text="Nie ma akutalnie odtwarzanej piosenki",justify="center",width=500,fg_color="gray")
        self.songName.place(x=250,y=500)
        browseButton=customtkinter.CTkButton(master=self.listSongFrame, text='Przeglądaj',hover_color="green",fg_color="gray", command=self.ButtonBrowse)
        browseButton.pack(padx=0.5, pady=0.5)
        customtkinter.CTkButton(master=self.listSongFrame, text='Powrót', command=lambda:self.mainMenu.tkraise()).pack()
        
        self.Listbox.bind("<Double-1>",self.activateSong) 

    def creatingSongForListbox(self):
        i=0
        for filename in os.listdir(self.activeDirectory):
             i=i+1
             self.Listbox.insert(i,filename)
    def activateSong(self,event):
        # Sama aktywacja wciśniętej piosenki
        self.controler.reloadJson()
        select=self.Listbox.curselection()
        name=self.Listbox.get(select)
        self.songName.configure(text=name) #Zmienienie Nazwy piosenki, w dolnej części ekranu
        self.enableButtons() # Odszarzenie przycisków
        # Czyszczenie kolejek 
        self.controler.queue.previousQueue_random = []
        self.controler.queue.songs_queue_loop = [] 
        self.controler.queue.songs_queue_random =[]
        self.controler.getSongUrl("{}/{}".format(globaly.activeDirectory,name))
        self.controler.playSong() # Odtworzenie piosenki
        # Zmiana Znaku play na pause 
        if self.Pause_unpause.buttonState == (-1):
            self.Pause_unpause.click_function()
    
    def setVolume(self,volume):
        #Ustawienie głośności 
        volume=self.volumeScale.get()
        self.controler.setVolume(volume/500)

    
    def buttonStopAction(self):
        # Akcja zatrzymania piosenki po wciśnięciu przycisku stop
        self.songName.configure(text="Nie ma akutalnie odtwarzanej piosenki")
        self.disableButtons() # Wyszarzenie przycisków
        self.controler.stopSong()
    def buttonPauseAction(self):
        self.controler.PauseUnpauseSong()

    def getNameFromUrl(self):
        tempList=[]
        temp=self.controler.song.get_url()
        nameSong=""
        for s in reversed(temp):
            if s != "/":
                tempList.insert(0,s)
            else:
                break
        nameSong=nameSong.join(tempList)
        return nameSong
    def buttonNextAction(self):
        # Odtworzenie następnego utworu w kolejce w zależności od stanu kolejki 
        self.controler.playNext(self.LoopRandom.buttonState)
        name=self.getNameFromUrl()
        self.songName.configure(text=name)
        if self.Pause_unpause.buttonState == (-1):
            self.Pause_unpause.click_function()
    def buttonPreviousAction(self):
        #Odtworzenie poprzedniej piosenki z playlisty
        self.controler.playPrevious()
        name=self.getNameFromUrl()
        self.songName.configure(text=name)

    def buttonLoopRandomAction(self):
        #Pusta funkcja 
        pass

    def ButtonBrowse(self):
        directory = filedialog.askdirectory(title="Wybierz folder")
        if directory == "":
            return
        self.activeDirectory=directory
        globaly.activeDirectory=self.activeDirectory
        self.Listbox.delete(0,"end")
        self.creatingSongForListbox()
        self.controler.reloadJson()

    def printVolume(self,event):
        # Getter głośności 
        self.volume=self.volumeScale.get()

    def enableButtons(self):
        #Aktywacja przycisków
        self.Pause_unpause['state']="normal"
        self.Stop['state']="normal"
        self.Next['state']="normal"
        self.Previous['state']="normal"

    def disableButtons(self):
        #Dezaktywacja przyciskow
        self.Pause_unpause['state']="disabled"
        self.Stop['state']="disabled"
        self.Next['state']="disabled"
        self.Previous['state']="disabled"

    
    def addSong(self):
        #Dodanie nowej piosenki
        newSong=self.getSongUrl()
        temp=self.downolader.download_to_mp4(newSong)
        name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp4'.format(temp)
        target_name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp3'.format(temp)
        temp=temp.replace(",","")
        temp=temp.replace(".","")
        temp=temp.replace("'","")
        temp=temp.replace("'","")
        self.downolader.from_mp4_to_mp3(name,target_name)
        self.Listbox.insert("end",("{}.mp3").format(temp))

        self.controler.reloadJson()



         




