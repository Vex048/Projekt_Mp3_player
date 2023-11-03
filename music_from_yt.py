from pytube import YouTube 
import os 
from moviepy.editor import *
download_directory='D:\PROJEKT_MP3_PLAYER\SONGS'

def download_mp3(url):
    url=YouTube(url)
    audio=url.streams.filter(only_audio=True).first()
    try:
        audio.download(download_directory)
        return str(audio.title)
    except:
        print("Failed to download audio")
    print("Song was downloaded")


def from_mp4_to_mp3(filename,name):
        video = AudioFileClip(filename)
        video.write_audiofile(name)
        os.remove(filename)



# for filename in os.listdir('D:\PROJEKT_MP3_PLAYER\SONGS'):
#     if filename[-4:] == ".mp3":
#          continue
#     from_mp4_to_mp3('D:\PROJEKT_MP3_PLAYER\SONGS\{}'.format(filename),'D:\PROJEKT_MP3_PLAYER\SONGS\{}.mp3'.format(filename[:-4]))
