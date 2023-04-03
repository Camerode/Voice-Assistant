# Voice-Assistant
Support and Community available at: https://discord.gg/EzVNGsBtd5


This software is a Voice Assistant, capable of performing actions (commands), such as taking a picture, getting the current weather and more!
It is being maintained and improved daily, and more features are being added. If you yourself would like your own Voice Assistant, then you've come to the right place.
The software uses python in version 3.9.13

## Documentation
Available on our Discord: https://discord.com/channels/1092081377500995644/1092142497779687566

## Collaborate and Contribution
If you'd like to collaborate, please contact "Camerode#4656" on Discord!

Contribution is available in:
- [Contribute](https://discord.com/channels/1092081377500995644/1092209412522901545)
- [Support](https://discord.com/channels/1092081377500995644/1092084770671960245)
- [Requests](https://discord.com/channels/1092081377500995644/1092086444442538076)


## Installation
Feel free to skip some sections if you already have anaconda installed (if you use python environments). Pip is required.
### Step 1 - Installing an IDE
An IDE allows you to edit code, debug, command line breaks, and track variables in a User Interface.
You can use almost any IDE that you wish, but specifically, Visual Studio Code is suggested.
Simply download from: <https://code.visualstudio.com/Download>
And run the download. This will turn it into an executable and is where all the programming will be done.

### Step 2 - Installing Anaconda & Python
Now, one needs to install Anaconda. Anaconda is a free, open-source distribution of Python and R programming languages for data science and machine learning. Specifically, it allows for python environments which is what we will be utilising. Go to: <https://www.anaconda.com/products/distribution> and download your version. Open the executable when it has been downloaded. You'll see a user interface open, click next, then "just me" (or "all" if you are going to be using multiple user accounts, not recommended). Next, choose the installation location, e.g. on Windows: `C:\ProgramData\Anaconda3` and click next. 

In the following section, if you're installing python for the first time, click both boxes, this allows for command lines in the command prompt/terminal application. If you already have it installed, only tick the "Register Anaconda as my default python...".
And now click install...

To check if it is installed, open "Command Prompt" or "Terminal" and type: `python --version`, if an error comes up, you've got a problem, you'd better research it, if not, then great, that's the boring part out the way!

### Step 3 - Setting up an environment
Now, here's where it gets a little more in-depth, during this process, do not close the command prompt or terminal.
Open "Command Prompt" or "Terminal", what we're going to do is create an environment to run the Voice Assistant, think of this as a private house specifically for one use. In the Prompt/Terminal, write: `conda create -n VirtualAssistant python=3.9.13`. Let it load for a bit, it will ask if you're sure that you wish to make this environment, type `y` and hit enter. This will set up the environment.

This environment will be used to install the python dependencies to allow the Voice Assistant to run.

### Step 4 - Visual Studio Code
Each IDE is different, but do the same thing. However, starting off, open Visual Studio Code and click clone repository from GitHub, search for `Camerode/Voice-Assistant`, now click: `View` -> `Command Palette` -> `Python: Select Interpreter` -> `Python 3.9.13 ('Voice Assistant')...`. This has selected the environment for us to install the package. If we were to change the environment were to change, the packages would not be installed.

### Step 5 - Installing Requirements
This part is entertaining to watch (from personal experience)..., in Visual Studio Code, click `Terminal` on the top bar, and `New Terminal`, in that terminal run: `pip install -r requirements.txt`. If it didn't install, then the repository wasn't cloned properly.

### Step 6 - Run the program
The main executable file is `VA.py`, simple open that file and click the small `>` arrow in the top right, enjoy!

Please note that some features require administrator permission to be able to run like the "computer statistics" command.
![Logo](https://imgur.com/zJV3u4K.jpg)
