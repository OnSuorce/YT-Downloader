import PySimpleGUI as sg
import modules.video_download as video_download
import modules.audio_download as audio_download
import modules.thumbnail as thumbnail
import os
from PIL import Image 
import io
sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Text('Insert URL'), sg.InputText(key="-URL INPUT-", enable_events=True)],
            [sg.Button('DOWNLOAD'), sg.Button('Cancel'),sg.Text('File type: '),sg.OptionMenu(values=('MP4', 'MP3'),  k='-FILE TYPE-')],
            [sg.Image(key="-THUMBNAIL-")],

            ]
            

# Create the Window
window = sg.Window('YouTube Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(event)

    if(event == "-URL INPUT-" and len(values["-URL INPUT-"]) > 24 ):
        thumbnail.get_thumbnail(values["-URL INPUT-"])
        if os.path.exists("thumbnail.jpg"):
           image = Image.open("thumbnail.jpg")
           image.thumbnail((400, 400))
           bio = io.BytesIO()
           image.save(bio, format="PNG")
           window["-THUMBNAIL-"].update(data=bio.getvalue())


    if(event == "DOWNLOAD"):

        if(values['-FILE TYPE-'] == "MP4" ):
            print(values["-URL INPUT-"])
            video_download.download(values["-URL INPUT-"])
    
        if(values['-FILE TYPE-'] == "MP3" ):
            print(values["-URL INPUT-"])
            audio_download.download(values["-URL INPUT-"])

window.close()