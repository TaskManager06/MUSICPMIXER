from faulthandler import dump_traceback
from tkinter import *
import tkinter as tk
from playsound import playsound
import multiprocessing
import os
from multiprocessing import Process
import keyboard
import sys
import time
from colorama import init, Fore, Back, Style
init(convert=True)
print(""""

         _____   _______   ______   __  __    ____    _____    _                  __     __  ______   _____  
  / ____| |__   __| |  ____| |  \/  |  / __ \  |  __ \  | |          /\     \ \   / / |  ____| |  __ \ 
 | (___      | |    | |__    | \  / | | |  | | | |__) | | |         /  \     \ \_/ /  | |__    | |__) |
  \___ \     | |    |  __|   | |\/| | | |  | | |  ___/  | |        / /\ \     \   /   |  __|   |  _  / 
  ____) |    | |    | |____  | |  | | | |__| | | |      | |____   / ____ \     | |    | |____  | | \ \ 
 |_____/     |_|    |______| |_|  |_|  \____/  |_|      |______| /_/    \_\    |_|    |______| |_|  \_\
                                                                        
        """)


def Piano():
    playsound('path')


def Vocals():
    playsound('path')


def Drums():
    playsound('path')


def Guitar():
    playsound('path')


global p
global v
global D
global G
global Pianobool
global Guitarbool
global Drumbool
global Vocalbool


p = multiprocessing.Process(target=Piano)

v = multiprocessing.Process(target=Vocals)
D = multiprocessing.Process(target=Drums)
G = multiprocessing.Process(target=Guitar)
Pianobool = False
Guitarbool = False
Drumbool = False
Vocalbool = False


def adw():
    print('test')


def STEMO():
    if __name__ == '__main__':
        print(1)
        root = tk.Tk()

        def PlayPiano():

            global Pianobool
            if Pianobool:
                global p
                p.terminate()
                Pianobool = False
                print('Paused')
                p = multiprocessing.Process(target=Piano)

            elif not Pianobool:
                p.start()
                print('Started')
                Pianobool = True
                p.join

        def PlayVocal():

            global Vocalbool
            if Vocalbool:
                global v
                v.terminate()
                Vocalbool = False
                print('Paused')
                v = multiprocessing.Process(target=Vocals)

            elif not Vocalbool:
                v.start()
                print('Started')
                Vocalbool = True
                v.join

        def PlayDrums():

            global Drumbool
            if Drumbool:
                global D
                D.terminate()
                Drumbool = False
                print('Paused')
                D = multiprocessing.Process(target=Drums)

            elif not Drumbool:
                D.start()
                print('Started')
                Drumbool = True
                D.join

        def PlayGuitar():

            global Guitarbool
            if Guitarbool:
                global G
                G.terminate()
                Guitarbool = False
                print('Paused')
                G = multiprocessing.Process(target=Guitar)

            elif not Guitarbool:
                G.start()
                print('Started')
                Guitarbool = True
                G.join()

        while True:

            root.title('STEMOPLAYER')
            root.geometry("700x700")
            root.config(bg='#212124')
            Pianobutton = Button(root, bg='#007aff', fg='white',
                                 text='Piano', height=25, width=25, command=(PlayPiano))
            Pianobutton.place(x=550, y=250)
            Guitarbutton = Button(root, bg='#007aff', fg='white',
                                  text='Guitar', height=5, width=30, command=(PlayGuitar))
            Guitarbutton.place(x=270, y=570)
            rumbutton = Button(root, bg='#007aff', fg='white',
                               text='Drums', height=25, width=25, command=(PlayDrums))
            rumbutton.place(x=10, y=250)
            vocalbutton = Button(root, bg='#007aff', fg='white',
                                 text='Vocals', height=5, width=30, command=(PlayVocal))
            vocalbutton.place(x=270, y=210)
            title = Label(root, text="STEMOPLAYER", bg='#212124', fg='white')
            title.config(font=("Courier", 80, ))
            title.place(x=0, y=100)
            root.mainloop()


STEMO()
