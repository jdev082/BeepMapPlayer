#!/usr/bin/env python3
import os
import string
import time
import sys
rep_array = []
start_rep = False

command_root = "beep"
freq_arg = "-f"
length_arg = "-l"

if len(sys.argv) > 2:
    print("ERR: Too many arguments!")
    sys.exit()
elif len(sys.argv) < 2:
    print("ERR: Too few arguments!")
    sys.exit()

def getchar(string, n):
    return str(string)[n - 1]

try:
    open(sys.argv[1])
except FileNotFoundError:
    print("ERR: File specified could not be found!")
    sys.exit()

with open(sys.argv[1]) as beepmap:
    while beepmap.readable():
        for line in beepmap:
            if "RPD" in line.strip():
                def_rep = getchar(line.strip(), 4)
                print(def_rep)
            if line.strip() == 'REPEAT_START':
                start_rep = True
                break
            if line.strip() == 'REPEAT_STOP':
                start_rep = False
                break
            if start_rep == True:
                rep_array.append(line)
                for x in rep_array:
                    for i in range(int(def_rep)):
                        if "DEL" in line:
                            if "." in line:
                                time.sleep(float(line[3:]))
                            else:
                                time.sleep(int(line[3:]))
                            break
                        note = x[:3]
                        length = x[3:]
                        os.system(f'{command_root} {freq_arg} {note} {length_arg} {length}')
                        print(f'PLAYING: {x}')
                break
            if "RPD" not in line:
                if "DEL" in line:
                    if "." in line:
                        time.sleep(float(line[3:]))
                    else:
                        time.sleep(int(line[3:]))
                    break
                note = line[:3]
                length = line[3:]
                os.system(f'{command_root} {freq_arg} {note} {length_arg} {length}')
                print(f'PLAYING: {line}')
        print(start_rep)
        print(rep_array)
