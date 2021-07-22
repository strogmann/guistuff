import io
import os
import PySimpleGUI as sg
from PIL import Image #importing any necessary os information, interface, and image library to pick up images

sg.theme('DarkAmber')
file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")] #selecting image formats for the program, in this case those of which that are supported by Pillow
def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File"),
            sg.Input(size=(25, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"), #selecting a designated image file fitting the description of the chunk above 
        ],
    ]
    window = sg.Window("Image Viewer", layout) #window name
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED: #permitting user to close program by pressing 'x' button on window
            break
        if event == "Load Image": 
            filename = values["-FILE-"]
            if os.path.exists(filename): #condition for supported file formats
                image = Image.open(values["-FILE-"])
                image.thumbnail((400, 400))
                byte = io.BytesIO()
                image.save(byte, format="PNG")
                window["-IMAGE-"].update(data=byte.getvalue()) #generating image from the file directory that the user has selected
    window.close() #theoretically, once all instances halt, the window will close, but they never stop until induced manually through closing window
if __name__ == "__main__":
    main()