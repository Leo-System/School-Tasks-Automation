'''
The purpose of this code is to say the screen size of the computer and to show to position of where the mouse cursor is.
'''

import pyautogui as pa
import os 
'''
The os library is here just to clear the terminal, so, to do this in Unix systems and in Windows systems, the code bellow detect the
user os and put the respective comand in a variable, so i can can only the variable later in the code.
'''

if(os.name == 'posix'):
    clear = 'clear'
else:
    clear = 'cls'


def screenSize():
    os.system(clear)
    width, height = pa.size()
    print(f"The width of your monitor is: {width}\nAnd the heigth is {height}")
    input("Press anything to continue.") 

def mousePosition():
    while(True):
        try:
            print(pa.position())
        except KeyboardInterrupt:
            print("\nStoping showing the cursor position.\n")
            input("Press any key to continue")
            break

#Main:
while(True):
    os.system(clear)
    #The op variable recives a string because this way i don't need to care about the user inserting a char in a intanger variable.
    op = input("Choose a option:\n1 - See the screen size;\n2 - Show the mouse cursor position;\nAny other key - Exit the program.")

    if(op == '1'):
        screenSize()
    elif(op == '2'):
        mousePosition()
    else:
        os.system(clear)
        break
