import PySimpleGUI as sg
import modules.video_download as video_download
import modules.audio_download as audio_download
import modules.thumbnail as thumbnail
import os
from PIL import Image 
import io

sg.theme('Black')   

# Layout.
layout = [ 
            [sg.Text("")],
            [sg.Text('Insert URL'), sg.InputText(key="-URL INPUT-", enable_events=True)],
            [sg.Column(layout=[[sg.Text("",key="-ERRORS-",text_color= "red")]], justification="center")],
            [sg.Text('Format: '), sg.OptionMenu(values=('MP4', 'MP3'),  k='-FILE TYPE-'), sg.Text('Resolution: '), sg.OptionMenu(values=('Highest','Lowest'),  k='-RES-')],
            [sg.Image(key="-THUMBNAIL-", size=(300, 300))],
            [sg.Column(layout= [[sg.Button('DOWNLOAD',key="-DOWNLOAD-", size=(12,3), disabled=True)]], justification='center')]
            ]
            


window = sg.Window('YouTube Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        try:
            os.remove("thumbnail.jpg")
        except:
            pass 

        break
    print(event)

    if(event == "-URL INPUT-" and len(values["-URL INPUT-"]) > 24 ): #if user inputs something longer than 24 chars
        
        if(thumbnail.get_thumbnail(values["-URL INPUT-"])): #loads thumbnail
        
            image = Image.open("thumbnail.jpg")
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-THUMBNAIL-"].update(data=bio.getvalue())
            window["-DOWNLOAD-"].update(disabled=False)


    if(event == "-DOWNLOAD-"): #if user presses download button
        window['-ERRORS-'].update("")
        print(values['-FILE TYPE-'])
        
        if(values['-FILE TYPE-'] == "MP4" and values['-RES-'] != ""): #video
            print(values["-URL INPUT-"])
            video_download.download(values["-URL INPUT-"],values["-RES-"])
    
        if(values['-FILE TYPE-'] == "MP3" ): #audio
            print(values["-URL INPUT-"])
            audio_download.download(values["-URL INPUT-"])
        
        if(values["-RES-"] == ""):
            window['-ERRORS-'].update("Select a valid resolution if you wish to download a video")
        if(values['-FILE TYPE-'] == ""):#Errors
            window['-ERRORS-'].update("Select a valid format")
        
window.close()