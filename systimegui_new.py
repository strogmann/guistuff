import os, keyboard, PySimpleGUI as sg, datetime, time #imports, as usual
from pynput import keyboard

def timeNow(): #function to define timeNow variable
    systime = time.strftime("%H:%M:%S") #changing the received system time from a float to a string going only to the second and not microsecond
    return systime

print(timeNow()) #prints current time in console for troubleshooting reasons
sg.theme ('DarkAmber') #theme


layout = [ #layout of the interface, including a static text, a dynamic output showing the time at the end, and an exit button
    [sg.Text('The current time is: ')],
    [sg.Output(key='-OUTPUT-')],
    [sg.Button('Exit')]
]
window = sg.Window('System Clock by Nicholas Martin', layout, finalize = False, keep_on_top=True, grab_anywhere=True) #setting what will appear on the window; just ordering, layout, and tab

while True: 
    event, values = window.read(timeout=1000) #the bit allowing timeNow to refresh later on

    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':  #if exit button or 'x' button on window tab are pressed, loop will break and stop the program
        break

    else: 
        window['-OUTPUT-'].update(timeNow()) #updates to new timeNow value
window.Refresh() #refreshes the window to show new time
window.close() #closes window