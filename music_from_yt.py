from pytube import YouTube 
import os 
from moviepy.editor import *
download_directory='D:\PROJEKT_MP3_PLAYER\SONGS'

# def download_mp3(url):
#     url=YouTube(url)
#     audio=url.streams.filter(only_audio=True).first()
#     try:
#         audio.download(download_directory)
#         return str(audio.title)
#     except:
#         print("Failed to download audio")
#     print("Song was downloaded")


# def from_mp4_to_mp3(filename,name):
#         video = AudioFileClip(filename)
#         video.write_audiofile(name)
#         os.remove(filename)



class downloader_from_youtube: # Class which is gonna download a file from yt
     download_directory=""
     def __init__(self):
          self.download_directory="D:\PROJEKT_MP3_PLAYER\SONGS"
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

            



# class downloaderG:
#     def __init__(self):
#         self.download_directory="D:\PROJEKT_MP3_PLAYER\SONGS"
#     def downlaod(self,url):
#         yt = YouTube(str(url))
#         video = yt.streams.filter(only_audio=True).first()
#         out_file = video.download(output_path=self.download_directory)  
#         base, ext = os.path.splitext(out_file) 
#         new_file = base + '.mp3'
#         os.rename(out_file, new_file) 
#         print("DOne")