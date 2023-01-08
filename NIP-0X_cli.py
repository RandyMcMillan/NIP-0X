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
            [sg.Input(key='-INPUT1-')],
            [sg.Text("What is the salting to be hashed?")],
            [sg.Input(key='-INPUT2-')],
            [sg.Text("What is the index to be hashed?")],
            [sg.Input(key='-INPUT3-')],
            [sg.Text(size=(40,1), key='-OUTPUT1-')],
            [sg.Button('Ok')] ]

def help():
    print('NIP-0x.py <base_entropy>')
    print('NIP-0x.py <base_entropy> <password_salting>')
    print('NIP-0x.py <base_entropy> <password_salting> <integer_index>')
    print('NIP-0X_cli.py ""')
    print('NIP-0X_cli.py " "')
    print('NIP-0X_cli.py "  "')

def hash_string(arg_array):
    """
    Return a SHA-256 hash of the given string
    """
    # print(len(arg_array))
    if len(arg_array) <= 2:
        # handled in main
        # length
        # 1             2
        # NIP-0X_cli.py <base_entropy>
        # arg_array[]
        # 0             1
        help()
    if len(arg_array) == 3:
        # length
        # 1             2              3
        # NIP-0X_cli.py <base_entropy> <password_salting>
        # arg_array[]
        # 0             1              2
        # print(arg_array[0])
        # print(arg_array[1])
        # print(arg_array[2])
        return hashlib.sha256(arg_array[1].encode('utf-8') \
        + arg_array[2].encode('utf-8')).hexdigest()
    if len(arg_array) == 4:
        # length
        # 1             2              3                  4
        # NIP-0X_cli.py <base_entropy> <password_salting> <integer>
        # arg_array[]
        # 0             1              2                  3
        # print(arg_array[0])
        # print(arg_array[1])
        # print(arg_array[2])
        # print(arg_array[3])
        return hashlib.sha256(arg_array[1].encode('utf-8') \
        + arg_array[2].encode('utf-8') \
        + arg_array[3].encode('utf-8')).hexdigest()
    if len(arg_array) >= 5:
        # length
        # 1             2              3                  4         5
        # NIP-0X_cli.py <base_entropy> <password_salting> <integer> <nope>
        print("<base_integer> <password-salting> <index>")
        print("The index <integer> is an integer - but is hashed as a string.")
        help()
    else:
        help()

def main_cli(arg_array, window):
    # Do something with the information gathered
    window['-OUTPUT1-'].update('Hello ' + values['-INPUT1-'] + "! Thanks for trying PySimpleGUI")
    print('', hash_string(arg_array))

def main_gui():

    window = sg.Window('NIP-0X', layout)
    while True:
        event, arg_array = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        main_cli(arg_array, window)
        window.close()
        exit()
        # end main_gui

if __name__ == '__main__':
    values = []
    if len(sys.argv) < 2:
        # length
        # 1
        # NIP-0X_cli.py
        main_gui()
    if len(sys.argv) == 2:
        # length
        # 1             2
        # NIP-0X_cli.py <base_entropy>
        print(hashlib.sha256(str(sys.argv[1]).encode('utf-8')).hexdigest())
        exit()
    if len(sys.argv) == 3:
        # print(sys.argv[0])
        # print(sys.argv[1])
        # print(sys.argv[2])
        main_cli(sys.argv)
        exit()
    if len(sys.argv) == 4:
        # print(sys.argv[0])
        print(sys.argv[1])
        print(sys.argv[2])
        print(sys.argv[3])
        main_cli(sys.argv)
        exit()
    else:
        help()
        exit()