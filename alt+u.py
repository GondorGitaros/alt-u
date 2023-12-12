import keyboard
import time
import os
import shutil
import subprocess

FOLDER_LOCATION = "D:\\Code\\Git\\Main\\jslearn\\"
COUNTER_FILE_LOCATION = "D:\\Code\\Git\\Main\\alt+u\\counter.txt"
INDEX_HTML_PATH = "D:\\Code\\Git\\Main\\jslearn\\index.html"
STYLE_CSS_PATH = "D:\\Code\\Git\\Main\\jslearn\\style.css"

def addone():
    with open(COUNTER_FILE_LOCATION, 'r+') as file:
        counter = int(file.read())
        file.seek(0)
        file.write(str(counter + 1))
        file.truncate()
    return str(counter + 1)

def main():
    while True:
        time.sleep(0.05)
        if keyboard.is_pressed('alt + u'):
            counter = addone()
            path = os.path.join(FOLDER_LOCATION, counter)
            JS_PATH = os.path.join(path, "app.js")
            os.mkdir(path)        
            shutil.copyfile(INDEX_HTML_PATH, os.path.join(path, "index.html"))
            shutil.copyfile(STYLE_CSS_PATH, os.path.join(path, "style.css"))
            subprocess.run(["code.cmd", JS_PATH], check=True)

if __name__ == "__main__":
    main()