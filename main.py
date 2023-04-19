from faulthandler import dump_traceback
from tkinter import *
from playsound import playsound
import multiprocessing
import os
from multiprocessing import Process
import keyboard
import sys
import time
from colorama import init, Fore, Back, Style
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    path = os.path.dirname(__file__)
    print(""""
            _____   _______   ______   __  __    ____    _____    _                  __     __  ______   _____
    / ____| |__   __| |  ____| |  \/  |  / __ \  |  __ \  | |          /\     \ \   / / |  ____| |  __ \
    | (___      | |    | |__    | \  / | | |  | | | |__) | | |         /  \     \ \_/ /  | |__    | |__) |
    \___ \     | |    |  __|   | |\/| | | |  | | |  ___/  | |        / /\ \     \   /   |  __|   |  _  /
    ____) |    | |    | |____  | |  | | | |__| | | |      | |____   / ____ \     | |    | |____  | | \ \
    |_____/     |_|    |______| |_|  |_|  \____/  |_|      |______| /_/    \_\    |_|    |______| |_|  \_\
        """)

    def Piano():
        playsound(path + '/6.mp3')

    def Vocals():
        playsound(path + '/2.mp3')

    def Drums():
        playsound(path + '/3.mp3')

    def Guitar():
        playsound(path + '/5.mp3')
    p = multiprocessing.Process(target=Piano)
    v = multiprocessing.Process(target=Vocals)
    D = multiprocessing.Process(target=Drums)
    G = multiprocessing.Process(target=Guitar)

    def PlayPiano():
        if Pianobool:
            p.terminate()
            Pianobool = not Pianobool
            print('Paused')
            p = multiprocessing.Process(target=Piano)
        elif not Pianobool:
            p.start()
            print('Started')
            Pianobool = True
            p.join

    def PlayVocal():
        if Vocalbool:
            v.terminate()
            Vocalbool = not Vocalbool
            print('Paused')
            v = multiprocessing.Process(target=Vocals)
        elif not Vocalbool:
            v.start()
            print('Started')
            Vocalbool = True
            v.join

    def PlayDrums():
        if Drumbool:
            D.terminate()
            Drumbool = not Drumbool
            print('Paused')
            D = multiprocessing.Process(target=Drums)
        elif not Drumbool:
            D.start()
            print('Started')
            Drumbool = True
            D.join

    def PlayGuitar():
        if Guitarbool:
            G.terminate()
            Guitarbool = not Guitarbool
            print('Paused')
            G = multiprocessing.Process(target=Guitar)
        elif not Guitarbool:
            G.start()
            print('Started')
            Guitarbool = True
            G.join

    print(1)

    def loop():
        nummer = 0
        Pianobool = False
        Guitarbool = False
        Drumbool = False
        Vocalbool = False
        while True:
            if keyboard.is_pressed('G'):
                time.sleep(1)
                PlayGuitar()
                print(1)
            if keyboard.is_pressed('V'):
                time.sleep(1)
                PlayVocal()
            if keyboard.is_pressed('D'):
                time.sleep(1)
                PlayDrums()
            if keyboard.is_pressed('P'):
                time.sleep(1)
                PlayPiano()
            if keyboard.is_pressed('o'):
                break
            if Guitarbool == False:
                GuitarColor = Fore.RED
            if Guitarbool == True:
                GuitarColor = Fore.GREEN
            if Drumbool == False:
                Drumcolor = Fore.RED
            if Drumbool == True:
                Drumcolor = Fore.GREEN
            if Vocalbool == False:
                Vocalcolor = Fore.RED
            if Vocalbool == True:
                Vocalcolor = Fore.GREEN
            if Pianobool == False:
                Pianocolor = Fore.RED
            if Pianobool == True:
                Pianocolor = Fore.GREEN
            nummer = nummer + 1
            if nummer == 10000:
                print(Fore.WHITE + ' Guitar is ' + GuitarColor + str(Guitarbool), Fore.WHITE + ' Drum is ' + Drumcolor + str(Drumbool) +
                      Fore.WHITE + ' vocal is ' + Vocalcolor + str(Vocalbool), Fore.WHITE + ' Piano is ' + Pianocolor + str(Pianobool))
                nummer = 0
    loop()


init(convert=True)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)

   # root = Tk()
   # Pianobutton = Button(root,text='Piano',command=(PlayPiano))
   # Pianobutton.pack()
   # Guitarbutton = Button(root,text='Guitar')
   # Guitarbutton.pack()
   # rumbutton = Button(root,text='Drums')
   # rumbutton.pack()
   # ocalbutton = Button(root,text='Vocals')
   # ocalbutton.pack()
   # root.mainloop()s
