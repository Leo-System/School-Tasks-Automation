import pyautogui as pa
import time

#Because i use i3wm, i use the windows key as my mod key, so i put the value 'win' in a variable named mod so the code makes more sense
#with the i3 setup.
mod = 'win'

#Going to the 10° virtual desktop
pa.hotkey(mod, '0')

#wating a little bit
time.sleep(0.1)

#Now the code below will open firefox searching for his name in the packege searcher
pa.hotkey(mod, 'd')
pa.write("firefox")
pa.press("enter")

#Wating a little bit more
time.sleep(5)

#Now that firefox has opened, the code can go to chatgpt.com, that is what the code below do
pa.write('chatgpt.com', interval=0.1) #Here needs a minimal interval between each letter writen so the code can press enter normaly in the next line
pa.press('enter')

#This time the code will need to wait longer because chatgpt will take a bit to open
time.sleep(25)
