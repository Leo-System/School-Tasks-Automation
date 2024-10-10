# __School-Tasks-Automation__

This is a code that automate school homework. It is made using python and PyAutoGui and pyperclip. Note that it uses the setup of my computer to work (that is a Arch Linux with i3wm with no customization in the window layout), so have in mind that it is made to work in my computer.

## __About the code__

This is a RPA project about automating school homework, it asks the user about how many themes he needs to search and it automate the process of going to a ia, making a initial prompt to direct the behavior of the ai and asking it to write a text about the themes.

> [!NOTE]
> This code will make the ai write paragraphs and only paragraphs, so have this in mind when running the code.

## __What you need to to run the code__

The function of the code is based on my setup, if you want to run the code you will need to have the following:

1. A 1366x768 screen size monitor;
2. i3wm as your desktop enviroment without heavy customization (mine have praticaly none, i only changed the fonts of the system);
3. The windows key as your mod key (this is the key that will do the i3 comands, you can alter the code in the line 15 if you want to run on your setup);
4. Arch Linux as your OS.

> [!NOTE]
> This code has been only been tested on a computer with Arch Linux and i3wm, it is possible that it can run on other Linux Os that have i3wm as it desktop enviroment.

## __How to run the code__

> [!WARNING]
> The first 3 steps are about preparing to run the code in your machine, like downloading the libraries, their dependencies and making a python virtual enviroment. If you already done them before you can skip them.

1. Download the dependencies of the libraries needed with the comand `sudo pacman -S xclip python-xlib scrot` so the libraries can execute their comands (This comand is used if you will run the code on a arch based Linux distro, if you will run it on other distro you will need to search how to install them in your distro);

2. Create a virtual enviroment for python if you don't have one so you can download the Libraries needed and run the code;
    - To create the virtual enviroment first run `python3 -m venv ~/<your ambient name>`, change <your ambient name> to the name that you want it to have (if you want you can put a dot in the front of the name so the directory of it became a hiden directory).
    - After creating it run the comand `source ~/<your ambient name>/bin/activate` to run the virtual enviroment. When it is activated you can download the libraries needed and run the code (__NOTE:__ the libraries will be downloaded in the venv, so if you make another one they will note be there);
    - When you finished downloading the libraries and running the program run the comand `deactivate` to exit the virtual enviroment.

> [!TIP]
> Because these comands for the virtual enviroment are big, you can create a alias to call them when you need.

3. In the virtual enviroment, download the libraries PyAutoGui and pyperclip with the comand `pip install pyautogui pyperclip`;

4. Still in the virtual enviroment, go to the code directory and run it with `python3 automatization.py`.

## __Libraries used__

The Libraries used in this project and their function are:

1. __PyAutoGui__:
    - This Librarie is used to automate the actions on the computer, so the code do the asking part for the user;

2. __Pyperclip__:
    - This library is used in the cases that the code will write down some text that contains somethings that the user has writed, this is done so pyperclip copy the text containing the users entries and PyAutoGui do a "ctrl + v" comand. This is done because, if the user insert something with special carachter when the code will write it down it will write the special carchters, unlike "pyautogui.write()" that cannot write special carachters.

3. __time__:
    - This library is used in some cases to make the code stop, so it can wait something, like the browser open or the ai say something.

4. __os__:
   - This library is only used in the stating of the program to clear the terminal.
