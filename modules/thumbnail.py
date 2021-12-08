
import requests
from pytube import YouTube
from PIL import Image
import io

def get_thumbnail(url):
    try:
        img_url = YouTube(url).thumbnail_url
        print(img_url)
        img_data = requests.get(img_url).content
        with open('thumbnail.jpg', 'wb') as handler:
            handler.write(img_data)
        
        return "io.getvalue()"
    except:

        return "not a valid url"