#!/usr/bin/env python3
import sys
import cryptography as cr
import hashlib
import PySimpleGUI  as sg

tab1_layout = [
#             [sg.Text('Key Generator')],
              [sg.Text("base_entropy")],
              [sg.Input(key='-INPUT1-')],
              [sg.Text("password_salt")],
              [sg.Input(key='-INPUT2-')],
              [sg.Text("index")],
              [sg.Input(key='-INPUT3-')],
              [sg.Text('', size=(64,1), key='-BASE-')],
              [sg.Text('', size=(64,1), key='-BASEOUTPUT-')],
              [sg.Text('', size=(64,1), key='-BASEPW-')],
              [sg.Text('', size=(64,1), key='-BASEPWOUTPUT-')],
              [sg.Text('', size=(64,1), key='-BASEPWIDX-')],
              [sg.Text('', size=(64,1), key='-BASEPWIDXOUTPUT-')],
              [sg.Button('Ok'), sg.Button('Quit')]
              ]


tab2_layout = [[sg.Text('Tab 2')]]
tab3_layout = [[sg.Text('Tab 3')]]
tab4_layout = [[sg.Text('Tab 3')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [[sg.Tab('Key Gen', tab1_layout, key='-TAB1-'),
                     sg.Tab('Tab 2', tab2_layout, visible=False, key='-TAB2-'),
                     sg.Tab('Tab 3', tab3_layout, key='-TAB3-'),
                     sg.Tab('Tab 4', tab4_layout, visible=False, key='-TAB4-')]]
# The window layout - defines the entire window
layout = [[sg.TabGroup(tab_group_layout,
                        enable_events=True,
                        key='-TABGROUP-')]]

# Create the window
window = sg.Window('NIP-0X', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.Read()
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