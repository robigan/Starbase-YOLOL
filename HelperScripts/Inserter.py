from pyautogui import press, write, keyDown, keyUp
from sys import argv
from time import sleep
from requests import get

METHOD = None
CONTENT = None

def wait():
    print("Waiting 5 seconds before proceeding...")
    sleep(5)
    print("Commencing...")

def printHelp():
    print("Usage: program {web | manual} [contents]")
    print("Method(s): {Web | Manual | Clear}")

try:
    METHOD = argv[1]
    METHOD = METHOD.lower()
except:
    print("Please specify a mode after calling the script (Like this: python3 ./Insterter.py manual)")
    exit(1)

try:
    CONTENT = argv[2]
except:
    print("No content specified...")

def main():
    if METHOD == "manual": # Manually input code
        if CONTENT == None:
            user_input = input("Code to paste: ")
            user_input = iter(user_input.splitlines())

        wait()

        for line in user_input:
            write(user_input, interval=0.01)
            press("down")
        exit(0)
    elif METHOD == "web": # Gets the code directly from the web
        if CONTENT == None:
            url = input("URL to copy from: ")

        try: # Use requests to get the file and then "format" it
            file = get(url)
            file = file.text
            file = iter(file.splitlines())
        except:
            print("There was an error getting the file")
            exit(1)

        wait()

        for line in file:
            write(line, interval=0.01)
            press("down")
        exit(0)
    elif METHOD == "clear":
        wait()

        for _ in range(0,20):
            keyDown("ctrl")
            press("a")
            keyUp("ctrl")
            press("backspace")
            press("down")

    else:
        print("Program incorrect usage")
        printHelp()
        exit(1)
    
if __name__ == "__main__":
    main()