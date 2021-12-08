
from pytube import YouTube
from pytube.cli import on_progress
def download(url):
    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        for i in yt.streams:
            print(i)
        return yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    
    except:
        return "Error"

    
    
if __name__ == "__main__":
    print("You are not supposed to run this file")
    input("")