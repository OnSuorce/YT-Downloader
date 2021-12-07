import PySimpleGUI as sg
import YouTube


sg.theme('Black')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText(key="-URL-")],
            [sg.Button('DOWNLOAD'), sg.Button('Cancel')],
            [sg.Listbox(values = sg.theme_list(), 
                      size =(20, 12), 
                      key ='-THEME LISTBOX-',
                      enable_events = True)]
            ]
            

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print(event)
    if(event == "DOWNLOAD"):
        print(values["-URL-"])
        YouTube.download(values["-URL-"])

window.close()