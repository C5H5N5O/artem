from pywebio.platform.tornado import start_server
from pywebio.input import *
from pywebio.output import *

import serial 

directions = {
    "↑": "w",
    "←": "a",
    "→": "d",
    "↓": "s"
}

def send_serial(string):
    my_serial = serial.Serial('/dev/', 9000)
    my_serial.write(f"{string}".encode("utf-8")) 
    my_serial.close()



put_buttons(["↑", "←", "→", "↓"], onclick=lambda n : send_serial(directions[n]))

put_button("выровнять колёса", onclick=lambda: send_serial("z"))