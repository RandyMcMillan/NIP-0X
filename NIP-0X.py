#!/usr/bin/env python3
import sys
import argparse
import cryptography as cr
import hashlib
import PySimpleGUI  as sg
import pyqrcode
#import png
from PIL import Image
import webbrowser

close64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsSAAALEgHS3X78AAAE30lEQVRIiZ2VXYgdRRqGn6+quvucM/85iRoTNevMBJFEWY0GFQTBC1HBlaz/jMpoFFfXBdmFvdiLvRIEFRHFGBXMjUQhF/6Bol6sSNaIruCNir/R/Dlx5iRzck736e6qby/6JDlx9CIWFN10Ue/7vW+9X7XcDn8bryWPL2vERkNQQPj9Q72K7F3s7Hxb9bZ98L0bj91jt1y23kxNTxIEGUQ/aTYR6WW9cud/Prx01zf7/7FP5EHXHG7Y6bVTpBPLMSegCWKEEMKvkihgjEWDP+FbEjxTa1bjv9l/CsIKF3ypHhUDSFGACCKC956iKKjV6/hfkCjgUNK0TW1oCA3h+EJk8UUBYFCsQaSyRajArUWLnEONcTrT68nTLtZaEKmmMTiUlsREGy9HO0dgcL1y6lgtZrAsEYFexhwxq2buYfru+1mcOo+828UYg4rgUH7OSkY3zbDq1lkaV1yFP9TqEyy18jiBCMF7DjYmOOu+hxifnCSKItZuvp/F6fPJ05TEwE+dHhN33MfpGy4iFAVjf7qF8etvBV9y1IilBApGIMt6TExOM372JKqKqhLFMdOz93Jk6jx+bHVoztzLyj9eiHqP2Gq7O3UlGAuq1RwYDlUwhoChMdSAz3ZxaEeD8T/fBggaAnGtxpqZWdKFBSbOPLMCCQGJItJPdrHw4lOYRgNsBM6dSCDGErIuodtGkhoyPEr68U5svcbI1ZsQY0CV2vAw9ZGRKjEiSBTR/fQjDm9/AddcjqoSul182kYHVDhJauRffUH7wD7ilatxzVOwI6PM7XiJLO2x4rob0CgGVTSEKigidD94j/ltW9Dg0b0/4BfmyQ8ewKUdWLZ6wCIB9SXFXJvQ+hLkc6QeEznHf199jY1rpjh1w0ZUFTGm7z18/tSj2Hffor5shKLdhhJCADMcw7IlKRIkAqkJRIa4LPl6d5c/PPJkBd5vpArcArD+ue101l1Md08bFxuIBUlOyOUggUIAVIl94Kv5wKqtz7L+7r/0bRHEmApcFbwnHhljw6tv0b3kEtK5gDWmj/GbfQAWZbdaztjyPOfP3oN6D8GDCO133uDAvx9CyxKsRX1JMjbBBa+8Rnbl5RSpR35RfXUGfVLnYGFBcTfdwLo77yLkPYy14CLa773JngfuoNy7QOh2WPnw09WVkufUm8s598G/s+eT9wmBJZ1m+sVTFNBc4Wi8vJ3v//kAJk7AOhbf3MGezTfjWwuYCcv8s1s58K+/okWOxDGdjz5g7+YZtKRSoL+igCp5FKVntGk48sTTzDWb1C+4mB833wgETD2CELBjEfNbtyAjo4xdcz27N11L6B5GGoZQhN+26KiSoII9LebnJx9BkggzNIQkyfEdItiRQGvbM7S2bQHJMGN1NO8ds2dQhBORYBCjAFEE1kFSw0QxuAiTJCAGce64vz4gviTkOTJcErIMMRbyDIxg7bHTFnc47clcmpdj43VkeBRJEkytgdTqSL2OiRMkSRDroH9t4EtCUaBZhmYpIUurZ9pFfVnuX+w62xfjeq3D3/6vbifXrT1XkzgWdREmipA4RlwMUYRY21cg/X+lJ5gSbIHGOVovCHmOCSX7DrbMx599icIhVI2cA5c5mC1gbGnITm4oqAOr0PoOXs9g51HAGiITyCDByXDp4KuiaoESmP8/YC0Y5GajmEsAAAAASUVORK5CYII='

github64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAADAwMDQ0NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAhyjGAAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAADdUAAA3VAT3WWPEAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAABzSURBVChTbYxRFoAgDMPQ+98Z1zbIeJqPbU3RMRfDECqyGpjMg6ivT6NBbKTw5WySq0jKt/sHrXiJ8PwpAAVIgQGkwABSYAApMIAUGEAalFmK9UJ24dC1i7qdj6IO5F+xnxfLu0jS0c7kqxd3Dk+JY8/5AKFrLuM7mfCAAAAAAElFTkSuQmCC'
storage64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAABwcHDQ0NDg4ODw8PFxcXGRkZGhoaGxsbHh4eIyMjJSUlJiYmJycnKCgoMTExMjIyNTU1NjY2Nzc3AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAouNksgAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAADdQAAA3UAe+RuhUAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAAC5SURBVChTfZLbDsMgDEPpbb3TDv7/W7PYuAztYUeqhO2QAGowkXIMIeYkaSU4QsNBi4GcyhNINpTglmq4GWSphvy/ldkuLXZ4HmAxy3NmFJaA4guKGCwsjClfV05+fWdhYBtFw+amB292aygW3M7fsPTwjmadZkCvHEtWaAYTViBqVwgTA3tJVnB6D/xhaimItDhjMBvlhtFsaIafnEtOaAY/twAw/eslK70CbX8obUvgJNw9Jv0+Zh8D4s5+VAm/LwAAAABJRU5ErkJggg=='


def show_qr(hashed_base_pw_idx, window):
    s = hashed_base_pw_idx
    url = pyqrcode.create(s)
    img = s[0:14]
    url.png(img, scale=10)
    im = Image.open(img)
    im.show()
    # end show_qr


def save_qr(hashed_base_pw_idx, window):
    s = hashed_base_pw_idx
    url = pyqrcode.create(s)
    img = s[0:14]
    url.png(img, scale=10)
    # im = Image.open(img)
    # im.show()
    # end show_qr


# ------ BEGIN GUI Definition ------ #
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', '&Properties', 'E&xit']],
            ['&Edit', ['&Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Toolbar', ['---', 'Command &1', 'Command &2',
                          '---', 'Command &3', 'Command &4']],
            ['&Help', '&About...'], ]

sg.set_options(auto_size_buttons=True,
               margins=(0, 0), button_color=sg.COLOR_SYSTEM_DEFAULT)

toolbar_buttons = [[
    sg.Button('', image_data=close64[22:],
              button_color=('white',
                            sg.COLOR_SYSTEM_DEFAULT),
              pad=(0, 0),  key='-close-'),
    sg.Button('', image_data=github64[22:],
              button_color=('white',
                            sg.COLOR_SYSTEM_DEFAULT),
              pad=(0, 0), key='-github-'),
    sg.Button('', image_data=storage64[22:],
              button_color=('white',
                            sg.COLOR_SYSTEM_DEFAULT),
              pad=(0, 0), key='-storage-'),
    ]]
# end ShowMeTheButtons

tab1_layout = [
    # [sg.Text('Key Generator')],
    [sg.Text("BASE_ENTROPY")],
    [sg.Input(size=(100, 1), key='-INPUT1-')],
    [sg.Text("password • additional entropy")],
    [sg.Input(size=(100, 1), key='-INPUT2-')],
    [sg.Text("index (secret integer • hashed as a string)")],
    [sg.Input(size=(100, 1), key='-INPUT3-')],
    # [sg.Text('', size=(100, 1), key='-BASE-')],
    [sg.Text('', size=(100, 1), key='-BASEOUTPUT-')],
    # [sg.Text('', size=(100, 1), key='-BASEPW-')],
    [sg.Text('', size=(100, 1), key='-BASEPWOUTPUT-')],
    # [sg.Text('', size=(100, 1), key='-BASEPWIDX-')],
    [sg.Text('', size=(100, 1), key='-BASEPWIDXOUTPUT-')],
    [sg.Button('Ok'), sg.Button('Quit')]
    ]

tab2_layout = [[sg.Text('NIP ##  ')]]
tab3_layout = [[sg.Text('NIP ### ')]]
tab4_layout = [[sg.Text('NIP ####')]]

# The TabgGroup layout - it must contain only Tabs
tab_group_layout = [
    [
        sg.Tab('Key Gen', tab1_layout, key='-TAB1-'),
        sg.Tab('NIP ##  ', tab2_layout, visible=True, key='-TAB2-'),
        sg.Tab('NIP ### ', tab3_layout, visible=True, key='-TAB3-'),
        sg.Tab('NIP ####', tab4_layout, visible=True, key='-TAB4-')
    ]
]

# The window layout - defines the entire window
layout = [
         [sg.Menu(menu_def, )],
         [sg.Frame('', toolbar_buttons,
                   title_color='white',
                   background_color=sg.COLOR_SYSTEM_DEFAULT, pad=(3, 3))],
    # [sg.Text('', size=(100, 0))],
         [sg.TabGroup(tab_group_layout,
                      enable_events=True,
                      key='-TABGROUP-')],
         [sg.Text('Status Bar',
                  relief=sg.RELIEF_SUNKEN,
                  size=(100, 1),
                  pad=(3, 3),
                  key='-status-')]
         ]

# Create the window
window = sg.Window('NIP-0X', layout)
# ------ END GUI Definition ------ #


def gui_loop(args):

#    window = sg.Window('NIP-0X', layout)
    event, values = window.Read()
    print(f"args.base_entropy: hashed_base={args.base_entropy}")
    window['-INPUT1-'].update(args.base_entropy)
    # Display and interact with the Window using an Event Loop
    while True:

        hashed_base = hashlib.sha256(
            str(values['-INPUT1-']).encode('utf-8')).hexdigest()

        print(f"gui_loop: hashed_base={hashed_base}")
        window['-INPUT1-'].update(args.base_entropy)
        # window['-BASEOUTPUT-'].update(BASE_ENTROPY)
        # window['-BASEOUTPUT-'].update('base_entropy:' + values['-INPUT1-'] + "")
        # window['-INPUT1-'].update(args.base_entropy)

        # event, values = window.Read()
        hashed_base_pw = hashlib.sha256(
            str(values['-INPUT1-']).encode('utf-8')
            + str(values['-INPUT2-']).encode('utf-8')).hexdigest()
        window['-BASEPWOUTPUT-'].update(hashed_base_pw)

        event, values = window.Read()
        hashed_base_pw_idx = hashlib.sha256(
            str(values['-INPUT1-']).encode('utf-8')
            + str(values['-INPUT2-']).encode('utf-8')
            + str(values['-INPUT3-']).encode('utf-8')).hexdigest()
        window['-BASEPWIDXOUTPUT-'].update(hashed_base_pw_idx)

        button, value = window.read()
        print(button)
        if button in ('-close-', 'Exit') or button is None:
            # break       # exit button clicked
            window.close()
            exit()
        print(button)
        if button == '-github-':
            url = 'https://github.com/RandyMcMillan/NIP-0X'
            webbrowser.open_new_tab(url)
            webbrowser.open_new(url)
            break
        print(button)
        if button == '-storage-':
            # url = 'https://github.com/RandyMcMillan/NIP-0X'
            save_qr(hashed_base_pw_idx, window)
            # webbrowser.open_new_tab(url)
            # webbrowser.open_new(url)
            break
        # See if user wants to quit or window was closed
        print(button)
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            # show_qr(hashed_base_pw_idx, window)
            break
            # Finish up by removing from the screen
            window.close()
            exit()


def main_cli(argv):
    print('main_cli')
    print(f'main_cli: command={argv}')
    # end main_cli


def main_gui(argv):
    # filename = sg.popup_get_file('Please enter a filename:')
    # main_cli(argv)
    print(f'main_gui: command={argv}')
    gui_loop(argv)
    # end main_gui


parser = argparse.ArgumentParser(
                    prog='NIP-0x_cli',
                    description='nostr python3 cli',
                    epilog='NOSTR is AWESOME!')
subparsers = parser.add_subparsers()
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                    help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                    const=sum, default=max,
#                    help='sum the integers (default: find the max)')
# parser.add_argument('--sum2', dest='accumulate2', action='store_const',
#                    const=sum, default=max,
#                    help='sum2 the integers (default: find the max)')
parser.add_argument('-g', '--gui',
                    dest='gui', action='store_true', default=False,
                    required=False,
                    help='Present GUI ')
parser.add_argument('-b', '--base',
                    dest='base_entropy',
                    type=str,
                    default='',
                    help='Your source of entropy type=str BASE_ENTROPY')
parser.add_argument('-pw', '--password',
                    dest='password', type=str, default='',
                    help='Addtional entropy type=str (BASE_ENTROPY+PASSWORD)')
parser.add_argument('-i', '--index',
                    dest='index', type=int, default='0',
                    help='Deterministic entropy \
                    type=str (BASE_ENTROPY+PASSWORD+INDEX)')
# end parser
args = parser.parse_args()
# print(f"test {args.integers}",args.accumulate(args.integers))
# print(f"args.accumulate(args.integers):",args.accumulate(args.integers))
args = parser.parse_args()
# print(vars(args))

if __name__ == '__main__':

    # print(f"{len(sys.argv)}", len(sys.argv))
    if args.base_entropy:
        print(args.base_entropy)
    if args.password:
        print(args.password)
    if args.index:
        print(args.index)
    print(f"{len(sys.argv)}", len(sys.argv))
    if len(sys.argv) < 2:
        main_cli(args)
        # end < 2
    # last
    if not args.gui:
        print(args.gui)
    if args.gui:
        print(args.gui)
        main_gui(args)
    if len(sys.argv) >= 2 and len(sys.argv) < 5:
        if sys.argv[1] == "-g" or sys.argv[1] == "--gui":
            main_gui(sys.argv)
        if sys.argv[1] == "-b" or sys.argv[1] == "--base":
            BASE_ENTROPY = sys.argv[2]
            main_cli(sys.argv)
        # end >= 2
    else:
        main_cli(sys.argv)
else:
    main_cli(sys.argv)