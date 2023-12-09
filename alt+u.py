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

def typethis(this):
    copy(this)
    keyboard.press('ctrl')
    time.sleep(0.1)
    keyboard.press('v')
    time.sleep(0.1)
    keyboard.release('v')
    time.sleep(0.1)
    keyboard.release('ctrl')
    time.sleep(0.1)
    keyboard.press('enter')
    time.sleep(0.1)
    keyboard.release('enter')

def s():
    time.sleep(0.4)

def open_terminal():
    time.sleep(0.5)
    keyboard.press('ctrl')
    s()
    keyboard.press('j')
    s()
    keyboard.release('j')
    s()
    keyboard.press('j')
    s()
    keyboard.release('j')
    s()
    keyboard.release('ctrl')


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
        s()
        typethis("cd ..")
        time.sleep(0.5)
        typethis(command1)
        s()
        typethis(command2)
        s()
        typethis(command6)
        s()
        typethis(command3)
        s()
        typethis(command4)
        s()
        addone()
        time.sleep(0.5)
