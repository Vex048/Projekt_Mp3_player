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



