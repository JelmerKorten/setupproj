## Readme

# Prerequisite
Python is installed.
Optional: Github is signed in in terminal and ready to use.
Optional: Your IDE.exe is added to path and can be opened with: code . or pycharm .
# Jump right in:
Sets up a new project folder and venv using the provided folder name.
To use:
- Copy the setupproj.py to your Projects folder or in which folder you want to create a new folder in.
- In terminal cd to the folder and run:
Windows:
python setupproj.py --f FOLDER [--open IDE] [--url url/to/repo.git]
MacOS:
python3 setupproj.py --f FOLDER [--open IDE] [--url url/to/repo.git]
# In Detail:
Uses standard path os.mkdir to create a new folder in the current directory.
If an url is provided it will use that to link to github repo. Prerequisite that github is signed in and ready to use in terminal.
It will create a virtual environment using pip with the same name as folder: .folder
If --open is provided it will attempt to open the IDE using either code . or pycharm .
