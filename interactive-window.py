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
          [sg.Text(size=(64,1), key='-OUTPUT1-')],
          [sg.Text(size=(64,1), key='-OUTPUT2-')],
          [sg.Text(size=(64,1), key='-OUTPUT3-')],
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
    hashed_base = hashlib.sha256(str(values['-INPUT1-']).encode('utf-8')).hexdigest()
    window['-OUTPUT1-'].update('base_entropy:' + values['-INPUT1-'] + "")
    window['-OUTPUT2-'].update(hashed_base)
    hashed_base_pw = hashlib.sha256(str(values['-INPUT1-']).encode('utf-8') \
    +str(values['-INPUT2-']).encode('utf-8')).hexdigest()
    window['-OUTPUT3-'].update(hashed_base_pw)

# Finish up by removing from the screen
window.close()