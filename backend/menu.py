import song
import Import_from_file
import Export_from_file
import music_from_yt
import queue_1
import threading
import time
import buttons
import tkinter as tk

class Menu:
    list_passable=[]
    is_active=True
    def __init__(self,root):
        self.is_active=True
        # root.geometry('1000x600')
        # root.title('Music player')
        # self.pauseButton=buttons.pauseButton('white',buttons.download_pause)
        # self.nextButton=buttons.nextButton('white',buttons.download_next)

    def printMenu(self):
        print("---------------------")
        print('Witaj w odtwarzaczu MP3!!\nWybierz jedną z dostępnych opcji poniżej')
        print('1.Załaduj pliki\n2.Wypisz wszystkie piosenki\n3.Wyjdź\n4.Dodaj piosenkę')
    def get_input(self):
            given_input = input()   
            return given_input
    
    def if_finished(self):
        try:
            song_current
        except NameError:
            return
        if song_current:
            if song_current.check_if_song_finished() == True:
                song_current.play_next_song(queue)
    
    def re_load_json(self):
        imported=Import_from_file.Importer()
        imported.import_mp3_to_json()
        self.check_for_passable_input()

    def start_thread(self,function):
        t1=threading.Thread(target=function)
        return t1

    def get_function_thread(self):
        while self.is_active == True:
            try:
                song_current
            except NameError:
                pass
            else:
                time.sleep(0.1)
                if song_current.check_if_song_finished() == True:
                    song_current.play_next_song(queue)
            


    def add_song(self):
        print("Wpisz url piosenki, którą chcesz dodać")
        new_song=input()
        if new_song=="0":
            return
        try:
            downloader_yt
        except NameError:
            downloader_yt=music_from_yt.downloader_from_youtube()
        x=downloader_yt.download_to_mp4(new_song)
        print(x)
        name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp4'.format(x)
        target_name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp3'.format(x)
        downloader_yt.from_mp4_to_mp3(name,target_name)

    def do_command(self,input1):
        match input1:
            case "1":
                self.re_load_json()
                print("Przeładowano plik json")
                self.printMenu()
            case "2":
                self.print_songs_on_console()
            case "3":
                self.is_active=False
            case "4":
                self.add_song()
                self.printMenu()                   
            case "p":               
                self.check_for_song_inputs(input1)
            case "s":
                self.check_for_song_inputs(input1)        
            case "v":
                self.check_for_song_inputs(input1)
            case 'n':
                self.check_for_song_inputs(input1)
            case _:
                print("Nie poprawny input")
        

    def print_songs_on_console(self):
            print("--------------\nWybierz numer piosenki, którą chcesz odsłuchać\n-------\nJeśli chcesz powrócić do menu wciśniej 0")
            exported=Export_from_file.Exporter()
            data=exported.read_from_json()
            for index,json in enumerate(data,1):
                print(index ,'Title:', json['title'])
            input=self.get_input()          
            
            new_input=self.songs_input_if_passable(input)
            if new_input == "0":
                self.printMenu()
                return
            
            self.choose_song_to_play(str(new_input))
            return
            
    def songs_input_if_passable(self,input_temp):
        if input_temp in self.list_passable:
            return input_temp           
        elif input_temp == "p" or input_temp =="s" or input_temp == "v" or input_temp == "n":
            self.check_for_song_inputs(input_temp)
            input_temp=self.get_input()
            return self.songs_input_if_passable(input_temp)
        elif input_temp == "0":
            self.printMenu()
            return "0"
        else:
            print("Nie poprawny input")
            input_temp=self.get_input()
            return self.songs_input_if_passable(input_temp)
            
        
    def check_for_song_inputs(self,input):
            try:
                match input:
                    case 'p':
                        song_current.pause_unpause_song()
                    case 's': 
                        song_current.stop_song()
                        print("Zatrzymano piosenke")
                        return  
                    case 'v':
                        print("Ustaw wartość dźwięku pomiędzy <0;1>")
                        while True:
                            volume=self.get_input()
                            volume=float(volume)
                            if volume >=0 and volume <=1:
                                song_current.set_volume(volume)
                                break
                            else:
                                print("Wpisz glośnosc jeszcze raz")
                    case 'n':
                        if song_current.play_next_song(queue) == 0:
                                print("Nie ma nic w playliscie")
                        else:
                            print("Odpalono nastepna piosenke z playlisty")

            except:
                print("Nie ma puszczanej żadnej piosneki")   


    def check_for_passable_input(self):
        expo=Export_from_file.Exporter()
        data_json=expo.read_from_json()
        for i in range(len(data_json)):
            self.list_passable.append(str(i+1))

    def get_currSong(self):
        try:
            song_current
            
        except:
            NameError
            print("Nie ma puszcanej piosneki")
        else:
            if song_current != None:
                return song_current
            else:
                print("NONE")

    def choose_song_to_play(self,input1):
        if input1 ==  "0":
            return
        exported=Export_from_file.Exporter()
        data=exported.read_from_json()
        for index,json in enumerate(data,1):          
            if int(input1) == int(index):
                print('Aktualna Piosenka to: ',json['title'])
                url='D:\PROJEKT_MP3_PLAYER\SONGS\{}'.format(json['title'])
                global queue
                queue=queue_1.Queue()
                queue.create_queue_from_file()
                queue.fill_up_queue(json['title'])
                global song_current
                song_current=song.Song(url)
                song_current.set_volume(0.1)
                song_current.play_song()
                print("Wciśnij p jeśli chcesz zpauzować/wznowić piosenke\nWciśnij s jeśli chcesz zatrzymać piosenke\nWciśnij 0 aby, wrocic do wyboru muzyki")
                print('Wciśnij v jesli chcesz zmienic glośnosc')
                print("Wciśnij n jeśli chcesz przesunąć o jedną piosenkę do przodu")      
                while True:
                    queue.check_for_songs_queue(song_current)
                    if song_current.check_if_finished() == True:
                        break
                    input_song=self.get_input()
                    match input_song:
                        case 'p':
                            song_current.pause_unpause_song()
                        case 's': 
                            song_current.stop_song()
                            print("Zatrzymano piosenke")
                            self.print_songs_on_console()
                            return
                        case '0':                            
                            self.print_songs_on_console()
                            return    
                        case 'v':
                            print("Ustaw wartość dźwięku pomiędzy <0;1>")
                            while True:
                                volume=self.get_input()
                                volume=float(volume)
                                if volume >=0 and volume <=1:
                                    song_current.set_volume(volume)
                                    break
                                else:
                                    print("Wpisz glośnosc jeszcze raz")  
                        case 'n':
                            if song_current.play_next_song(queue) == 0:
                               print("Nie ma nic w playliscie")
                            else:
                               print("Odpalono nastepna piosenke z playlisty")                                                                              
                        case _ :
                            print("Nie poprawny input")
    
            
 