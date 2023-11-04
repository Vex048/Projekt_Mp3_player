import song
import Import_from_file
import Export_from_file
import music_from_yt
class Menu:
    list_passable=[]

    def __init__(self):
        print("---------------------")
        print('Witaj w odtwarzaczu MP3!!\nWybierz jedną z dostępnych opcji poniżej')
        print('1.Załaduj pliki\n2.Wypisz wszystkie piosenki\n3.Wyjdź\n4.Dodaj piosenkę')
        
    def get_input(self):
            given_input = input() 
            #current_input=self.if_input_correct(given_input)  
            return given_input
    
            
    def re_load_json(self):
        imported=Import_from_file.Importer()
        imported.import_mp3_to_json()
        self.if_input_passable()

    def add_song(self):
        print("Wpisz url piosenki, którą chcesz dodać")
        new_song=input()
        x=music_from_yt.download_mp3(new_song)
        print(x)
        name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp4'.format(x)
        target_name='D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp3'.format(x)
        music_from_yt.from_mp4_to_mp3(name,target_name)

    def do_command(self,input1):
        while True:
            match input1:
                case "1":
                    self.re_load_json()
                    print("Przeładowano plik json")
                    self.__init__()
                case "2":
                    self.print_songs_on_console()
                case "3":
                    exit()
                case "4":
                    self.add_song()
                    self.__init__()

                case _:
                    print("Nie poprawny input")
            self.do_command(self.get_input())


            


    def print_songs_on_console(self):
            print("--------------\nWybierz numer piosenki, którą chcesz odsłuchać\n-------\nJeśli chcesz powrócić do menu wciśniej 0")
            exported=Export_from_file.Exporter()
            data=exported.read_from_json()
            for index,json in enumerate(data,1):
                print(index ,'Title:', json['title'])
            input=self.get_input()
            self.choose_song_to_play(input)
            return
            
           
    def if_input_passable(self):
        expo=Export_from_file.Exporter()
        data_json=expo.read_from_json()
        for i in range(len(data_json)):
            self.list_passable.append(str(i+1))



    def choose_song_to_play(self,input):
        exported=Export_from_file.Exporter()
        data=exported.read_from_json()
          
        
        while True:
            if input == "0":
                self.__init__()
                return
            if input not in self.list_passable:
                print("Nie poprawny input")
                input=self.get_input()
            else:
                break
        for index,json in enumerate(data,1):          
            if int(input) == int(index):
                print('Aktualna Piosenka to: ',json['title'])
                #url='D:\PROJEKT_MP3_PLAYER\SONGS2\{}'.format(json['title'])
                url='D:\PROJEKT_MP3_PLAYER\SONGS\{}'.format(json['title'])
                song1=song.Song(url)
                song1.set_volume(0.1)
                song1.play_song()
                print("Wciśnij p jeśli chcesz zpauzować/wznowić piosenke\nWciśnij s jeśli chcesz zatrzymać piosenke\nWciśnij 0 aby, wrocic do wyboru muzyki")
                print('Wciśnij v jesli chcesz zmienic glośnosc')
                
                while True:
                    input_song=self.get_input()
                    match input_song:
                        case 'p':
                            song1.pause_unpause_song()
                        case 's': 
                            song1.stop_song()
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
                                    song1.set_volume(volume)
                                    break
                                else:
                                    print("Wpisz glośnosc jeszcze raz")
                                

                                                           
                        case _ :
                            print("Nie poprawny input")
        print("KONIEC PIOSENKI")
            
        
      
            
menu=Menu()
menu.if_input_passable()
menu.do_command(menu.get_input())





        