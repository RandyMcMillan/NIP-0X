#!/usr/bin/env python3
#apt-get install python-tk OR python3-tk
#OR
#make init
import cryptography as cr
import PySimpleGUI  as sg                        # Part 1 - The import
import hashlib

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()


# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")
print('Hello', hash_string(values[0]), "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()           