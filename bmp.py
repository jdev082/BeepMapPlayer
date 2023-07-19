#!/bin/bash
import os
import string
import time
import sys
rep_array = []
start_rep = False

if len(sys.argv) != 1:
    print('ERR: Too many or too few arguments!')
    print('bmp /path/to/beepmap.txt')
    exit()

def getchar(string, n):
    return str(string)[n - 1]

with open('beepmap.txt') as beepmap:
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
                        os.system(f'beep -f {note} -l {length}')
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
                os.system(f'beep -f {note} -l {length}')
                print(f'PLAYING: {line}')
        print(start_rep)
        print(rep_array)
