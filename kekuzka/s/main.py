from pywebio.platform.tornado import start_server
from pywebio.input import *
from pywebio.output import *
from functools import partial
import pyautogui as pg
import pyperclip, time


commands = ["m!p https://www.youtube.com/watch?v=JFGPSKLegeU&ab_channel=RedAleRT", "m!p трактор"]

def write(text: str):    
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    pg.hotkey("ctrl", "v")
    pyperclip.copy(buffer)


def write_command(text):
    pg.click()
    write(text)
    pg.press("enter")

def main():
    put_button(commands[0], onclick=lambda: write_command(commands[0]))
    put_button(commands[1], onclick=lambda: write_command(commands[1]))



if __name__ == "__main__": 
    start_server(main, debug=True, port=8080, cdn=False)