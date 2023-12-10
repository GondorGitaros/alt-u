import keyboard
import time
import pyperclip

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

def press(keybind):
    keyboard.press(keybind)
    s()

def release(keybind):
    keyboard.release(keybind)
    s()

def typethis(this):
    copy(this)
    press('ctrl')
    press('v')
    release('v')
    release('v')
    press('enter')
    release('enter')

def open_terminal():
    time.sleep(0.5)
    press('ctrl')
    press('j')
    release('j')
    press('j')
    release('j')
    release('ctrl')


#get counter
with open('counter.txt', 'r') as file:
    counter = file.read()


print(counter)


while True:
    time.sleep(0.05)
    if keyboard.is_pressed('alt + u'):
        command1 = "mkdir " + counter
        command2 = "cp index.html " + counter + "/index.html"
        command3 = "cd " + counter
        command4 = "code app.js "
        command6 = "cp style.css " + counter + "/style.css"
        open_terminal()
        typethis("cd D:\Code\Git\Main\jslearn")
        time.sleep(0.5)
        typethis(command1)
        typethis(command2)
        typethis(command6)
        typethis(command3)
        typethis(command4)
        addone()
        time.sleep(0.5)
