#!/usr/bin/env python3
import sys
import cryptography as cr
import hashlib
import PySimpleGUI  as sg

# Define the window's contents
layout = [
          [sg.Text("base_entropy")],
          [sg.Input(key='-INPUT1-')],
          [sg.Text("password_salt")],
          [sg.Input(key='-INPUT2-')],
          [sg.Text("index")],
          [sg.Input(key='-INPUT3-')],

          [sg.Text(size=(64,1), key='-BASE-')],
          [sg.Text(size=(64,1), key='-BASEOUTPUT-')],

          [sg.Text(size=(64,1), key='-BASEPW-')],
          [sg.Text(size=(64,1), key='-BASEPWOUTPUT-')],

          [sg.Text(size=(64,1), key='-BASEPWIDX-')],
          [sg.Text(size=(64,1), key='-BASEPWIDXOUTPUT-')],

          [sg.Button('Ok'), sg.Button('Quit')]
          ]

# Create the window
window = sg.Window('NIP-0X', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    hashed_base = hashlib.sha256( \
    str(values['-INPUT1-']).encode('utf-8')).hexdigest()
    # window['-OUTPUT1-'].update('base_entropy:' + values['-INPUT1-'] + "")
    window['-BASEOUTPUT-'].update(hashed_base)

    hashed_base_pw = hashlib.sha256( \
    str(values['-INPUT1-']).encode('utf-8') \
    +str(values['-INPUT2-']).encode('utf-8')).hexdigest()
    window['-BASEPWOUTPUT-'].update(hashed_base_pw)

    hashed_base_pw_idx = hashlib.sha256( \
    str(values['-INPUT1-']).encode('utf-8') \
    +str(values['-INPUT2-']).encode('utf-8') \
    +str(values['-INPUT3-']).encode('utf-8')).hexdigest()
    window['-BASEPWIDXOUTPUT-'].update(hashed_base_pw_idx)

# Finish up by removing from the screen
window.close()