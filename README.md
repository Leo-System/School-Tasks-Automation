# __School-Tasks-Automation__

This is a code that automates school homework. It is made using Python, PyAutoGui, and pyperclip. Note that it uses the setup of my computer to work (which is Arch Linux with i3wm and no customization in the window layout), so keep in mind that it is designed to work on my machine.

## __About the Code__

This is an RPA project focused on automating school homework. It asks the user how many topics they need to search for and automates the process of accessing an AI, making an initial prompt to direct its behavior, and asking it to write a text about the topics.

> [!NOTE]
> This code will make the AI write paragraphs and only paragraphs, so keep this in mind when running the code.

## __What You Need to Run the Code__

The functionality of the code is based on my setup. If you want to run the code, you will need the following:

1. A 1366x768 screen size monitor;
2. i3wm as your desktop environment without heavy customization (mine has practically none; I only changed the system fonts);
3. The Windows key as your mod key (this is the key that will execute the i3 commands; you can alter the code on line 15 if you want to run it on your setup);
4. Arch Linux as your OS.

> [!NOTE]
> This code has only been tested on a computer with Arch Linux and i3wm. It is possible that it can run on other Linux OS versions that have i3wm as their desktop environment.

## __How to Run the Code__

> [!WARNING]
> The first three steps involve preparing to run the code on your machine, such as downloading the libraries, their dependencies, and setting up a Python virtual environment. If you have already completed these steps, you can skip them.

1. Download the dependencies of the libraries needed with the command `sudo pacman -S xclip python-xlib scrot` so that the libraries can execute their commands. (This command is used if you are running the code on an Arch-based Linux distro; if you are running it on another distro, you will need to search for how to install them for your system.)

2. Create a virtual environment for Python if you don't have one, so you can download the necessary libraries and run the code:
    - To create the virtual environment, first run `python3 -m venv ~/<your environment name>`, changing `<your environment name>` to the name you want it to have (if you prefer, you can add a dot in front of the name so the directory becomes a hidden directory).
    - After creating it, run the command `source ~/<your environment name>/bin/activate` to activate the virtual environment. When it is activated, you can download the necessary libraries and run the code. (__NOTE:__ The libraries will be downloaded in the venv, so if you create another one, they will not be there.)
    - When you finish downloading the libraries and running the program, run the command `deactivate` to exit the virtual environment.

> [!TIP]
> Because these commands for the virtual environment are lengthy, you can create an alias to call them when needed.

3. In the virtual environment, download the libraries PyAutoGui and pyperclip with the command `pip install pyautogui pyperclip`;

4. Still in the virtual environment, navigate to the code directory and run it with `python3 automatization.py`.

## __Libraries Used__

The libraries used in this project and their functions are:

1. __PyAutoGui__:
    - This library is used to automate actions on the computer, allowing the code to handle user input.

2. __Pyperclip__:
    - This library is used in cases where the code will write text that contains information entered by the user. Pyperclip copies the text containing the user's entries, and PyAutoGui executes a "ctrl + v" command. This approach is used because if the user inputs something with special characters, the code will write them correctly; unlike `pyautogui.write()`, which cannot handle special characters.

3. __time__:
    - This library is used in some cases to pause the code, allowing it to wait for events such as the browser opening or the AI responding.

4. __os__:
   - This library is only used at the start of the program to clear the terminal.

