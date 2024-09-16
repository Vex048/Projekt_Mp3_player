from pytube import YouTube 
import os 
from moviepy.editor import *
import sys
sys.path.insert(1, '../main')
import globaly


class downloader_from_youtube: # Class which is gonna download a file from yt
     download_directory=""
     def __init__(self):
          self.download_directory=globaly.activeDirectory
          self.counter=0
          
     def download_to_mp4(self,url):
        url=YouTube(url)
        audio=url.streams.filter(only_audio=True).first()
        try:
            audio.download(self.download_directory)
            return str(audio.title)
        except:
            print("Failed to download audio")
        print("Song was downloaded")     
     
     def from_mp4_to_mp3(self,filename,name):
        fname,ext=os.path.splitext(filename)
        fname=fname.replace(",","")
        fname=fname.replace(".","")
        fname=fname.replace("'","")
        fname=fname.replace("'","")
        video = AudioFileClip(fname+ext)
        video.write_audiofile(fname+".mp3")
        os.remove(fname+ext)
        print(fname+".mp3")

            

