#!/usr/bin/python3
'''
Run as: ./huimai.py
Required files: 
    /etc/lirc/lircd.conf.d/huimai.lircd.conf
'''
# lirc info see: https://www.lirc.org/html/lirc_client.html
import lirc  # if missing:   pip3 install lirc 

KEY_TYPE =    {"numeric", "direction", "special"}
KEY_DIR  =    {"left", "right", "up", "down"}
KEY_SPECIAL = {"star", "pound", "ok"}

class Key:
    def __init__(self, mytype, myvalue):
        self.type  = mytype
        self.value = myvalue

key_info = {"KEY_0": ("numeric", 0),
            "KEY_1": ("numeric", 1),
            "KEY_2": ("numeric", 2),
            "KEY_3": ("numeric", 3),
            "KEY_4": ("numeric", 4),
            "KEY_5": ("numeric", 5),
            "KEY_6": ("numeric", 6),
            "KEY_7": ("numeric", 7),
            "KEY_8": ("numeric", 8),
            "KEY_9": ("numeric", 9),

            "KEY_NUMERIC_STAR":  ("special", "*"),
            "KEY_NUMERIC_POUND": ("special", "#"),
            "KEY_OK":            ("special", "ok"),

            "KEY_LEFT":  ("direction", "<"),
            "KEY_RIGHT": ("direction", ">"),
            "KEY_UP":    ("direction", "^"),
            "KEY_DOWN":  ("direction", "v")
        }

def get_key():
    with lirc.RawConnection() as conn:
        press = conn.readline()

#   Typical response:
#   press = "0000000000ff38c7 00 KEY_OK HUIMAI"

    words = press.split()
#   print(key_info[words[2]])
    mykey = key_info[words[2]]
    return Key(mykey[0], mykey[1])

try:
    while True:
        key = get_key()
        print(key.value)
except KeyboardInterrupt:
    print()
