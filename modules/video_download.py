
from pytube import YouTube
from pytube.cli import on_progress
def download(url, res):
    try:
        yt = YouTube(url,on_progress_callback=on_progress)

        streams =  yt.streams.filter(progressive=True,file_extension='mp4',mime_type="video/mp4").order_by('resolution')
        
        if(res == "Highest"):
            

           print("Downloading with highest resolution")
           streams.desc().first().download()

        elif(res == "Lowest"):
            
            print("Downloading with lowest resolution")
            streams.asc().first().download()
    
    except Exception as ex:
        print("An error occurred "+ (str))
        return "Error"

    
    
if __name__ == "__main__":
    print("You are not supposed to run this file")
    input("Press enter to close")

    #https://www.youtube.com/watch?v=Afc_z1ShqJ0