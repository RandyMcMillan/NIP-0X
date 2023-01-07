#!/usr/bin/env python3
#apt-get/brew install python-tk OR python3-tk
#OR
#make init
import sys
import cryptography as cr
import hashlib
import PySimpleGUI  as sg

# Define the window's contents
layout = [
            [sg.Text("What is the string to be hashed?")],
            [sg.Input()],
            [sg.Text("What is the salting to be hashed?")],
            [sg.Input()],
            [sg.Text("What is the index to be hashed?")],
            [sg.Input()],
            [sg.Button('Ok')] ]

def help():
    print('python3 NIP-0x.py <string>')

def hash_string(string):
    """
    Return a SHA-256 hash of the given string
    """
    print(string[0])
    print(string[1])
    #print(string[2])
    print(len(string))
    if len(string) == 0:
        return hashlib.sha256().hexdigest()
    if len(string) == 1:
        return hashlib.sha256(string[0].encode('utf-8')).hexdigest()
    if len(string) == 2:
        return hashlib.sha256(string[0].encode('utf-8') + string[1].encode('utf-8')).hexdigest()
    if len(string) == 3:
        return hashlib.sha256(string[0].encode('utf-8')).hexdigest()
    else:
        help()

def main_cli(string):
    # Do something with the information gathered
    print('', hash_string(string))

def main_gui():

    window = sg.Window('Window Title', layout)

    event, values = window.read()

    main_cli(values)

    window.close()

if __name__ == '__main__':
    values = []
    if len(sys.argv) < 2:
        #print(len(sys.argv))
        #print(sys.argv[0])
        main_gui()
        exit()
    if len(sys.argv) == 2:
        print(sys.argv[0])
        print(sys.argv[1])
        print(hashlib.sha256(str(sys.argv[1]).encode('utf-8')).hexdigest())
        exit()
    if len(sys.argv) == 3:
        print(sys.argv[0])
        print(sys.argv[1])
        print(sys.argv[2])
        main_cli(sys.argv)
        exit()
    if len(sys.argv) == 4:
        print(sys.argv[0])
        print(sys.argv[1])
        print(sys.argv[2])
        print(sys.argv[3])
        main_cli(sys.argv)
        exit()
    else:
        help()
        exit()