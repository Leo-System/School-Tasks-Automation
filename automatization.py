import pyautogui as pa
import pyperclip
import time
import os

"""
0 - Starting the program.
"""

#Clearing the terminal so the execution of the code becomes more clean
os.system("clear")

#Because i use i3wm, i use the windows key as my mod key, so i put the value 'win' in a variable named mod so the code makes more sense
#with the i3 setup.
mod = 'win'

'''
1 - Asking the user some informations to say to the ai what to write about.
'''

#Asking the user the field of study of the themes that he wants the ai to say.
field = input("Insert the field of the themes you will search: ")
os.system("clear")
#Asking the user the language that he want the answers to be:
language = input("Insert the language that the ai should give you the answers: ")
os.system("clear")

#Creating a variable that will hold the value of how many themes the ai will search:
quantThemes = 0

#Asking the user how many themes it will be:
while(True): #This while is to create a loop that will force the user to insert a int value.
    try: 
        quantThemes = int(input("Insert how many themes you will as the ai to say: ")) #The reciving of how many themes will be is in a try catch so if the user does not insert a int value the code will loop until he inserts a correct value
        os.system("clear")
        break
    except(ValueError):
        print("Wrong value! Insert a intanger number.") #Showing a messege to the user that the value is wrong.
        input("Press anything to continue") #Stoping the code so he can read the the message and continue
        os.system("clear")

#Creating the array that will hold the themes:
themes = [0 for i in range(quantThemes)]

#Putting things int the array so the code can use later.
for i in range(quantThemes):
    themes[i] = input(f"Insert the {i+1}° theme you want the ai to say about: ")
    os.system("clear")

'''
2 - Opening the ai in a free virtual desktop and opening the ai.
'''

#Going to the 10° virtual desktop
pa.hotkey(mod, '0')

#wating a little bit
time.sleep(2)

#Now the code below will open firefox searching for his name in the packege searcher
pa.hotkey(mod, 'd')
time.sleep(1)
pa.write("firefox")
pa.press("enter")

#Wating a little bit more
time.sleep(10)

#Now that firefox has opened, the code can go to chatgpt.com, that is what the code below do
pa.write('chatgpt.com', interval=0.1) #Here needs a minimal interval between each letter writen so the code can press enter normaly in the next line
pa.press('enter')

#This time the code will need to wait longer because chatgpt will take a bit to open
time.sleep(20)

'''
3 - Writing the inicial prompt to say to the ai what it needs to do.
'''

#Now the code will click in the write bar of the ai to write the prompt:
#pa.click(x = 446, y = 687)

#Writing the initial prompt that will instruct how the ai should act:
pyperclip.copy(f"You will make texts only composed by paragraphs about some things of {field} and you will make these texts in {language}. You can only make texts composed by paragraphs and they need to be in {language}. If you understand, say 'I will help you with {field}' in {language}.")
pa.hotkey('ctrl', 'v')

#Sending this initial prompt to the ai:
#pa.click(x = 1040, y = 680)
pa.press("enter")

#Pausing the code a little bit more
time.sleep(7)

'''
4 - Inserting the themes that the ai should write a text about.
'''

#Now it will send the themes so the ai make the text about them:
for i in themes:
    pa.click(x = 446, y = 687)
    pyperclip.copy(f"Make a text about {i} in {language} that is composed only by paragraphs. This text needs to be complete and not too big, try to make him with 1 to 3 paragraphs. Focus on make the text about {i} complet, saying everything that is needed to to know about him but not being too long as a said. Remember that it needs to be in {language}.")
    pa.hotkey('ctrl', 'v')
    pa.click(x = 1040, y = 680)
    time.sleep(20)
