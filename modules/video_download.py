
from pytube import YouTube
from pytube.cli import on_progress
def download(url, res):
    try:
        yt = YouTube(url,on_progress_callback=on_progress)
        streams =  yt.streams.filter(progressive=True,file_extension='mp4',mime_type="video/mp4").order_by('resolution')
        
        if(res == "Highest"):
           streams.desc().first().download()
        elif(res == "Lowest"):
            streams.asc().first().download()
    
    except:
        return "Error"

    
    
if __name__ == "__main__":
    print("You are not supposed to run this file")
    input("")