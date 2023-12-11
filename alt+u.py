import keyboard
import time
import os
import shutil
import subprocess

FOLDER_LOCATION = "D:\\Code\\Git\\Main\\jslearn\\"
COUNTER_FILE_LOCATION = "D:\\Code\\Git\\Main\\alt+u\\counter.txt"
INDEX_HTML_PATH = "D:\\Code\\Git\\Main\\jslearn\\index.html"
STYLE_CSS_PATH = "D:\\Code\\Git\\Main\\jslearn\\style.css"

#increment counter by 1 and save it to counter.txt
def addone():
    with open(COUNTER_FILE_LOCATION , 'r') as file:
        counter = file.read()

    addone = counter.replace(counter, str(int(counter) + 1))

    with open(COUNTER_FILE_LOCATION, 'w') as file:
        file.write(addone)

#get counter
with open(COUNTER_FILE_LOCATION, 'r') as file:
    counter = file.read()

path = os.path.join(FOLDER_LOCATION, counter) + "\\"
JS_PATH = path + "app.js"


while True:
    time.sleep(0.05)
    if keyboard.is_pressed('alt + u'):
        os.mkdir(path)        
        shutil.copyfile(INDEX_HTML_PATH, (path + "index.html"))
        shutil.copyfile(STYLE_CSS_PATH, (path + "style.css" ))
        subprocess.run(["code.cmd", JS_PATH], check=True)
        addone()
