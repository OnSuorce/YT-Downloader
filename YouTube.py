
from pytube import YouTube
from pytube.cli import on_progress
def download(url):
    try:
        YouTube(url,on_progress_callback=on_progress).streams.first().download()
        yt = YouTube(url)
        return yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    
    except:
        return "Error"

    
    

if __name__ == "_main_":
    print("You are not supposed to run this file")