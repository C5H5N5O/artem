from pywebio.platform.tornado import start_server
from pywebio.input import *
from pywebio.output import *


commands = ["m!p https://www.youtube.com/watch?v=JFGPSKLegeU&ab_channel=RedAleRT", "m!p трактор"]

def write_data(data):
    with open("buffer.txt", "w") as f:
        f.writelines(data)
        print(data)


def main():
    put_button(commands[0], onclick=lambda: write_data(commands[0]))
    put_button(commands[1], onclick=lambda: write_data(commands[1]))


if __name__ == "__main__":
    start_server(main, debug=True, port=8080, cdn=False)