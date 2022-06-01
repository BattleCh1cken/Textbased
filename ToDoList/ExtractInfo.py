#Extract autmoatic entering and text based screen and add it into Help-Python.md
from os import system as sys
from getkey import getkey, keys
from random import randint
from cursor import hide
from replit import db

hide()

if "sc" not in db.keys(): db["sc"] = []
if "sb" not in db.keys(): db["sb"] = {}

reset = "\u001b[0m"

def rgb(fg = [255, 255, 255], bg = None):
    try: return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]};48;2;{bg[0]};{bg[1]};{bg[2]}m"
    except: return f"\033[38;2;{fg[0]};{fg[1]};{fg[2]}m"

def clear(): sys('clear')

clear()

cp = 5
bn = 5

x = 20
y = 19

boards = []
for i in range(y):
    boards.append([])
    
for i in boards:
    for j in range(x):
        i.append("  ")

def printboard(boards):
    for i in range(x): print("--", end = "")
    print("--")
    for i in boards:
        print("|" + "".join(i) + "|")
    for i in range(x): print("--", end = "")
    print("--")

cc = [255, 255, 255]
ccm = "decrease"

def printcc(cc):
    x = []
    for i in cc: x.append(str(i))
    return ", ".join(x)

char = rgb(fg = [100, 100, 100]) + "██" + reset
bg = "  "

while True:

    boards[bn][cp] = char

    clear()

    print("Color Changing Mode: " + ccm.title())
    print("Current Color: " + rgb(fg = cc) + "██" + reset + " ({})\n".format(printcc(cc)))

    print("'z' To View Controls\n")
    
    printboard(boards)
    
    key = getkey()

    if key == "w" or key == keys.UP:
        if bn != 0:
            boards[bn][cp] = bg
            bn -= 1

    if key == "s" or key == keys.DOWN:
        if bn != len(boards) - 1: 
            boards[bn][cp] = bg
            bn += 1

    if key == "a" or key == keys.LEFT:
        if cp != 0: 
            boards[bn][cp] = bg
            cp -= 1

    if key == "d" or key == keys.RIGHT:
        if cp != len(boards[0]) - 1: 
            boards[bn][cp] = bg
            cp += 1

    if key == "q":
        boards[bn][cp] = rgb(fg = cc) + "██" + reset
        if randint(0, 1) == 0:
            try: 
                if boards[bn - 1][cp] == bg and bn != 0: 
                    bn -= 1
            except: 
                if boards[bn + 1][cp] == bg and bn != len(boards) - 1:
                    bn += 1
        else:
            try: 
                if boards[bn][cp - 1] == bg and cp != 0: 
                    cp -= 1
            except: 
                if boards[bn][cp + 1] == bg and cp != len(boards[0]) - 1: 
                    cp += 1

    modealgo = {
        "decrease": "increase",
        "increase": "decrease"
    }

    if key == "r":
        if ccm == "increase" and cc[0] < 255: cc[0] += 1
        if ccm == "decrease" and cc[0] > 0: cc[0] -= 1
            
    if key == "g":
        if ccm == "increase" and cc[1] < 255: cc[1] += 1
        if ccm == "decrease" and cc[1] > 0: cc[1] -= 1
            
    if key == "b":
        if ccm == "increase" and cc[2] < 255: cc[2] += 1
        if ccm == "decrease" and cc[2] > 0: cc[2] -= 1
            
    if key == "m": ccm = modealgo[ccm]

    if key == "e":
        clear()
        if len(db["sc"]) == 0: 
            print("No Saved Colors!")
            input("\n[ENTER]")
            continue
        else:
            q = input("1: Equip Color\n2: Remove Color\n\nOption: ")
            clear()
            for i, v in enumerate(db["sc"]):
                print(str(i + 1) + ": " + rgb(fg = v) + "██ " + reset + printcc(v))
            if q == "1":
                e = input("\nColor: ")
                cc = db["sc"][int(e) - 1]
            if q == "2":
                r = input("\nColor: ")
                db["sc"].remove(db["sc"][int(r) - 1])

    if key == "c":
        clear()
        if len(db["sb"]) == 0: 
            print("No Saved Drawings!")
            input("\n[ENTER]")
            continue
        else:
            q = input("1: View Drawing\n2: Remove Drawing\n3: Equip Drawing\n\nOption: ")
            clear()
            print("Drawings:\n")
            for i in db["sb"]: print(i)
            if q == "1":
                v = input("\n(Exactly What It The Drawing Name Says) Drawing Name: ")
                print()
                printboard(db["sb"][v])
                input("\n[ENTER] ")
            if q == "2":
                r = input("\n(Exactly What It The Drawing Name Says) Drawing Name: ")
                del db["sb"][r]
            if q == "3":
                e = input("\n(Exactly What It The Drawing Name Says) Drawing Name: ")
                print("\nThis May Take A While Since This Is BETA")
                print("Loading Board..")
                found = False
                boards = db["sb"][e]
                for i, v in enumerate(boards):
                    for j, k in enumerate(v):
                        if not found:
                            if boards[i][j] == char:
                                boards[i][j] = bg
                                found = True

    if key == "t":
        if cc not in db["sc"]: db["sc"].append(cc)

    if key == "v":
        name = input("\n(Put Name The Same As Another To Override It)\nDrawing Name: ")
        db["sb"][name] = boards

    if key == "p": 
        bg = rgb(fg = cc) + "██" + reset
        for i, v in enumerate(boards):
            for j, k in enumerate(v):
                boards[i][j] = bg

    if key == "o":
        q = input("\nRGB Color (Seperated By Spaces, Example: 100 100 100): ")
        q = q.split()
        EEEEE = []
        for i in q: EEEEE.append(int(i))
        cc = EEEEE

    if key == "z":
        clear()
        input("Press 'q' To Draw\nWASD Or Arrow Keys To Move\n'r' To Add/Subtract Red To Current Color\n'g' To Add/Subtract Green To Current Color\n'b' To Add/Subtract Blue To Current Color\n'm' To Change Color Changing Mode\n'e' To Use Saved Colors\n't' To Save Current Color\n'c' To Use Saved Drawings\n'v' To Save Current Drawing\n'p' To Change Canvas Color To Current Color\n'o' To Manually Enter An RGB Color\n\n[ENTER] ")