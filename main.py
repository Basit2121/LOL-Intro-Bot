import time
from tkinter import *
import keyboard as keyboard
import numpy as np
import pyautogui
import mouse


def bot():
    i = 5
    while i != 0:
        print('Starting in...', i)
        i = i - 1
        time.sleep(1)
    time.sleep(np.random.uniform(0.1, 1))
    while not keyboard.is_pressed('k'):
        start = None
        while start is None:
            start = pyautogui.locateOnScreen('assets/start.png', grayscale=True, confidence=0.8)
            if start is not None:
                start = pyautogui.center(start)
                pyautogui.leftClick(start)
            else:
                print('Looking For Start...')
        time.sleep(np.random.uniform(0.1, 1))
        accept = None
        while accept is None:
            accept = pyautogui.locateOnScreen('assets/accept.png', grayscale=True, confidence=0.8)
            if accept is not None:
                accept = pyautogui.center(accept)
                pyautogui.leftClick(accept)
                time.sleep(8)
                pyautogui.leftClick(accept)
                time.sleep(8)
                pyautogui.leftClick(accept)
                time.sleep(8)
                pyautogui.leftClick(accept)
            else:
                print('Looking For Accept...')
        time.sleep(np.random.uniform(0.1, 3))
        champion = None
        while champion is None:
            champion = pyautogui.locateOnScreen('assets/champ.png', grayscale=True, confidence=0.8)
            time.sleep(2)
            if champion is not None:
                champion = pyautogui.center(champion)
                pyautogui.leftClick(champion)
            else:
                print('Looking For Champion...')
        time.sleep(np.random.uniform(0.1, 1))
        lock = None
        while lock is None:
            lock = pyautogui.locateOnScreen('assets/lockin.png', grayscale=True, confidence=0.8)
            if lock is not None:
                lock = pyautogui.center(lock)
                pyautogui.leftClick(lock)
            else:
                print('Looking For Lock In...')
        time.sleep(np.random.uniform(0.1, 1))
        time.sleep(120)
        pyautogui.leftClick(810, 460)
        time.sleep(np.random.uniform(0.1, 1))
        pyautogui.leftClick(810, 460)
        pyautogui.press('y')
        keyboard.release('y')
        time.sleep(np.random.uniform(0.1, 1))
        pyautogui.press('p')
        keyboard.release('p')
        time.sleep(np.random.uniform(0.1, 1))
        pyautogui.leftClick(316, 464)
        time.sleep(np.random.uniform(0.1, 0.5))
        pyautogui.leftClick(316, 464)
        keyboard.press('p')
        keyboard.release('p')

        cont = None
        x = 1538
        y = 928
        while cont is None:
            cont = pyautogui.locateOnScreen('assets/continue.png', grayscale=True, confidence=0.8)
            if cont is not None:
                cont = pyautogui.center(cont)
                pyautogui.leftClick(cont)
            else:
                mouse.click('left')
                time.sleep(2)
                mouse.click('left')
                keyboard.press('ctrl')
                keyboard.press('r')
                keyboard.release('ctrl')
                keyboard.release('r')
                time.sleep(np.random.uniform(1, 3))
                keyboard.press('ctrl')
                keyboard.press('q')
                keyboard.release('ctrl')
                keyboard.release('q')
                time.sleep(np.random.uniform(1, 3))
                keyboard.press('ctrl')
                keyboard.press('w')
                keyboard.release('ctrl')
                keyboard.release('w')
                time.sleep(np.random.uniform(1, 3))
                keyboard.press('ctrl')
                keyboard.press('e')
                keyboard.release('ctrl')
                keyboard.release('e')
                time.sleep(30)
                pyautogui.rightClick(x, y)
                pyautogui.leftClick(x, y)
                time.sleep(5)
                pyautogui.leftClick(x, y)
                mouse.click('left')
                time.sleep(1)
                mouse.click('right')
                time.sleep(30)
                x = x + 3
                y = y - 3
                keyboard.press('q')
                keyboard.release('q')
                time.sleep(np.random.uniform(0.1, 1))
                keyboard.press('w')
                keyboard.release('w')
                time.sleep(np.random.uniform(0.1, 1))
                keyboard.press('e')
                keyboard.release('e')
                time.sleep(np.random.uniform(0.1, 1))
                keyboard.press('r')
                keyboard.release('r')
                time.sleep(np.random.uniform(0.1, 1))
                keyboard.press('f')
                keyboard.release('f')
                time.sleep(np.random.uniform(0.1, 1))
                keyboard.press('d')
                keyboard.release('d')
        time.sleep(np.random.uniform(0.1, 1))
        play_again = None
        while play_again is None:
            play_again = pyautogui.locateOnScreen('assets/play_again.png', grayscale=True, confidence=0.8)
            if play_again is not None:
                time.sleep(2)
                play_again = pyautogui.center(play_again)
                pyautogui.leftClick(play_again)
                mouse.click('left')
                time.sleep(1)
                pyautogui.leftClick(play_again)
                mouse.click('left')
            else:
                print('Looking For Play Again...')


window = Tk()
window.title("CO-OP Bot")
window.configure(background='black')
lbl = Label(window, text="The Bot is for CO-OP vs AI Intro Mode Only", bg='black', fg='white', font=("Arial Bold", 20))
lbl.grid(column=0, row=0)
lbl02 = Label(window, text="", bg='black', fg='white', font=("Arial Bold", 10))
lbl02.grid(column=0, row=1)
lbl55 = Label(window, text="1.Run the bot as ADMINISTRATOR", bg='black', fg='white',
              font=("Arial", 15))
lbl55.grid(column=0, row=2)
lbl2 = Label(window, text="2.Make Sure That The LOL CLIENT SIZE IS  1280x720", bg='black', fg='white',
             font=("Arial", 15))
lbl2.grid(column=0, row=3)
lbl3 = Label(window, text="3.Make Sure That you are in the CO-OP vs AI Intro Lobby ", bg='black', fg='white',
             font=("Arial", 15))
lbl3.grid(column=0, row=4)
lbl4 = Label(window, text="4.If Queue is Dodged Cancel the Queue and Restart the bot", bg='black', fg='white',
             font=("Arial", 15))
lbl4.grid(column=0, row=5)
lbl5 = Label(window, text="5.Dont Touch the keyboard of Mouse After the BOT Accepts a match", bg='black', fg='white',
             font=("Arial", 15))
lbl5.grid(column=0, row=6)
lbl00 = Label(window, text="", bg='black', fg='white', font=("Arial Bold", 10))
lbl00.grid(column=0, row=7)
lbl11 = Label(window, text="Check The READ_ME.txt File for any Queries about the bot", bg='black', fg='white',
              font=("Arial Bold", 18))
lbl11.grid(column=0, row=8)
lbl01 = Label(window, text="", bg='black', fg='white', font=("Arial Bold", 10))
lbl01.grid(column=0, row=9)
btn = Button(window, text="Run", bg="black", fg="white", command=bot, font=("Arial", 20))
btn.grid(column=0, row=10)
lbl0 = Label(window, text="", bg='black', fg='white', font=("Arial Bold", 10))
lbl0.grid(column=0, row=11)
lbl6 = Label(window, text="Follow me on Twitter @basit192", bg='black', fg='white', font=("Arial Bold", 10))
lbl6.grid(column=0, row=12)
lbl7 = Label(window, text="Github Profile https://github.com/Basit2121", bg='black', fg='white',
             font=("Arial Bold", 10))
lbl7.grid(column=0, row=13)
window.geometry('700x500')
window.mainloop()
