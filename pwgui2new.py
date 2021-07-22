from os import read
import PySimpleGUI as sg
import random
import string


def passgen(length):
    lowerchar = string.ascii_lowercase
    upperchar = string.ascii_uppercase
    number = string.digits
    symbol = string.punctuation
    all = number + lowerchar + symbol + upperchar
    temp = random.sample(all, length)
    password = "".join(temp)
    return password


#conval = int(string)
#key = conval
length = sg.Input

#lower = string.ascii_lowercase
#upper = string.ascii_uppercase
#number = string.digits
#symbol = string.punctuation
 
#all = number + lower + symbol + upper

#temp = random.sample(all, length)
#password = "".join(temp)

#all = string.ascii_letters + string.digits + string.punctuation
#password = "".join(random.sample(all, length))

sg.theme ('DarkGrey4')
layout = [
          [sg.Text('Please select the desired length for your password:')],
          [sg.Slider(range=(4,30), default_value=12, orientation='horizontal')],
          [sg.Text('Your password is '), sg.Output(key='-OUTPUT-')],
          [sg.Button('OK')],
          [sg.Button('Exit')]
         ]
window = sg.Window('Strong Password Generator by Nicholas Martin', layout, finalize= True)

while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit': 
        break

    if event == 'OK' : 
        window['-OUTPUT-'].update(passgen(int(values[0])))

window.close()



