from pytube import YouTube
from pytube.cli import on_progress
def download(url):
    try:
        yt = YouTube(url)

        
        return yt.streams.get_audio_only().download(filename=f"{yt.title}.mp3")
    
    except:
        return "Error"

    
    

if __name__ == "__main__":
    print("You are not supposed to run this file")
    input("")