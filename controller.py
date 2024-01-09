from song import Song #Importowanie Klasy Piosenki
from queue_1 import Queue #Importowanie Klasy Kolejki
from pygame import mixer # Importowanie mixera, który służy do odtwarzania muzyki

from Import_from_file import Importer # Importowanie importera do jsona
class Controler:
    def __init__(self):
        #Konstruktor mixera oraz Klasy song i queue
        mixer.init()
        mixer.music.set_volume(0.1)
        self.song=Song()
        self.queue=Queue()
        self.stop=True
        
    
    def getSongUrl(self,url):
        # Wzięcie piosenki z Listboxa i przypsanie atrybutu url
        self.song.set_url(url)




    def check_if_song_finished(self):
        #Sprawdzanie czy dana piosenka się skończyła
        temp1=self.song.get_played()
        temp2=self.song.get_paused()
        if mixer.music.get_busy() == False and temp1==True and temp2==False:
            return True
        else:
            return False

    def playSong(self):
        #Odtworzenie piosenki

        temp=self.song.get_url()
        mixer.music.load(temp)
        mixer.music.play()
        self.createQueue(self.song)
        self.song.set_paused(False)
        self.song.set_played(True)
    
    def PauseUnpauseSong(self):
        #Zpauzowanie lub odpausowanie piosenki
        temp1=self.song.get_played()
        temp2=self.song.get_paused()
        if temp1==True and temp2==False:
            mixer.music.pause()
            self.song.set_paused(True)
        elif temp1==True and temp2==True:
            mixer.music.unpause()
            self.song.set_paused(False)
        
    def stopSong(self):
        #Zatrzymanie Piosenki
        temp=self.song.get_played()
        if temp == True:
            mixer.music.stop()
            self.song.set_played(False)
        self.stop=False


    def setVolume(self,volume):
        mixer.music.set_volume(volume)
            
        
    def createQueue(self,song):
        # Tworzenie poszczególnych kolejek dla odtwarzania random i loop
        self.queue.fill_up_queue_random(song)
        self.queue.fill_up_queue_loop(song)
        

            
        
    
    def playNext(self,loopState):
        # Granie Następnej piosenki w playliscie
        temp=self.song.get_url()
        self.queue.previousQueue_random.insert(0,temp) # umieszczenie w kolejce poprzednie piosenki
        self.queue.check_for_songs_queue(self.song) #Sprawdzenie czy znajduje się coś w queue, jesli nie to queue się wypełnia
        self.stopSong()
        #Sprawdzanie jaki jest stan przyczisku dla kolejek 
        if loopState == 1:
            new_url=self.queue.get_from_queue_random()
        else:
            new_url=self.queue.get_from_queue_loop()
        #self.song.url=new_url
        self.song.set_url(new_url)
        self.playSong()


    def playPrevious(self):
        #Odtwarzanie poprzedniej piosenki z playlisty
        if len(self.queue.previousQueue_random) == 0:
            return
        temp=self.song.get_url()
        self.queue.songs_queue_random.insert(0,temp)
        self.queue.songs_queue_loop.insert(0,temp)
        self.stopSong()
        previous_url=self.getFromPreviousQueue_random()
        self.song.set_url(previous_url)
        self.playSong()
    
    def getFromPreviousQueue_random(self):
        #Otrzymanie pierwwszej piosenki w kolecje previous 
        previousSong=self.queue.previousQueue_random[0]
        self.queue.previousQueue_random.pop(0)
        return previousSong
    

    
    def reloadJson(self):
        #Przeładowanie referencji do piosenk w jsonie
        imported=Importer()
        imported.import_mp3_to_json()







