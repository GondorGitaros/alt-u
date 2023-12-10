import keyboard
import time
import pyperclip

FOLDER_LOCATION = "D:\Code\Git\Main\jslearn"

#increment counter by 1 and save it to counter.txt
def addone():
    with open('counter.txt', 'r') as file:
        counter = file.read()

    addone = counter.replace(counter, str(int(counter) + 1))

    with open('counter.txt', 'w') as file:
        file.write(addone)

def copy(this):
    pyperclip.copy(this)

def s():
    time.sleep(0.4)

def pressandrelease(keybind):
    keyboard.press(keybind)
    time.sleep(0.3)
    keyboard.release(keybind)
    time.sleep(0.3)

def press(keybind):
    keyboard.press(keybind)
    s()

def release(keybind):
    keyboard.release(keybind)
    s()

def typethis(this):
    copy(this)
    press('ctrl')
    pressandrelease('v')
    release('ctrl')
    pressandrelease('enter')

def open_terminal():
    time.sleep(0.5)
    press('ctrl')
    pressandrelease('j')
    pressandrelease('j')    
    release('ctrl')

#get counter
with open('counter.txt', 'r') as file:
    counter = file.read()

while True:
    time.sleep(0.05)
    if keyboard.is_pressed('alt + u'):
        command1 = "mkdir " + counter
        command2 = "cp index.html " + counter + "/index.html"
        command3 = "cp style.css " + counter + "/style.css"
        command4 = "cd " + counter
        command5 = "code app.js "
        open_terminal()
        typethis("cd " + FOLDER_LOCATION)
        typethis(command1)
        typethis(command2)
        typethis(command3)
        typethis(command4)
        typethis(command5)
        addone()
