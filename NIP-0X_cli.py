#!/usr/bin/env python3.10
import pip
import sys, re, os, platform, shutil, stat, subprocess, os.path

while True:

    print('True')
    try:
        print('try')
        #import your modules here. !
        from argparse import ArgumentParser
        from ds_store import DSStore
        from mac_alias import Alias
        from pathlib import Path
        from subprocess import PIPE, run
        from typing import List, Optional
        from PySimpleGUI import *
        from PySimpleGUI_Events import *
        from tk import *
        from cryptography import *

        os.system('pip3 install cryptography')
        print('break')
        break

    except ImportError as err_mdl:

        #print((err_mdl.name))
        pip.main(['install', err_mdl.name])
    else:
        os.system('pip3 install -r requirements.txt')
        os.system('pip3 install .')

