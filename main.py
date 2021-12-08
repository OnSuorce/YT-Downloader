import PySimpleGUI as sg
import modules.video_download as video_download
import modules.audio_download as audio_download


sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [ 
            [sg.Text('Insert URL'), sg.InputText(key="-URL INPUT-", enable_events=True)],
            [sg.Button('DOWNLOAD'), sg.Button('Cancel'),sg.OptionMenu(values=('MP4', 'MP3'),  k='-FILE TYPE-')],
            [sg.Listbox(values = sg.theme_list(), 
                      size =(20, 12), 
                      key ='-THEME LISTBOX-',
                      enable_events = True)]
            ]
            

# Create the Window
window = sg.Window('YouTube Downloader', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(event)
    if(event == "DOWNLOAD" and values['-FILE TYPE-'] == "MP4" ):
        print(values["-URL-"])
        video_download.download(values["-URL-"])
    
    if(event == "DOWNLOAD" and values['-FILE TYPE-'] == "MP3" ):
        print(values["-URL-"])
        audio_download.download(values["-URL-"])

window.close()