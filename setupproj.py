    # SetupProj plots notams on a streetmap.
    # Copyright (C) 2023  Jelmer Korten (korty.codes)

    # SetupProj is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # SetupProj is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with SetupProj.  If not, see <https://www.gnu.org/licenses/>.

    # Contact: korty.codes@gmail.com

# setupproj
# To set up a project
# version 1.0.2

import sys
from os import system, mkdir, makedirs, chdir
from os.path import dirname, realpath, join
import platform
import shutil
import argparse

# To clear the terminal
clear = lambda: system("cls || clear")

def create_folder(full_path):
    """Creates a folder based on the fullpath provided.
    The full path is create based on the folder this file is ran in and the new foldername provided.
    Should that folder already exist it will ask you before overwriting.
    
    To Run:
    copy this file to the folder that holds all your projects / where you want to set up a new project:
    In terminal cd to the folder you want to setup the project
    python setupproj.py --f PROJECTNAME [--open vscode/pycharm] [--url GITHUB REPO URL]"""

    try:
        mkdir(full_path)
    except FileExistsError as err:
        print(err)
        print(f"Do you want to OVERWRITE the current information in {full_path}?")
        print("Yes/No")
        choice = input().lower()
    except FileNotFoundError as err:
        print(err)
        print("Creating folders...")
        makedirs(full_path)
        print("All folders in the path have been created.")
    else:
        print("Your folder has been created.")
    # finally will be run at the end of a try-except but I only will have choice
    # defined if the FileExistsError runs. So we check if choice in locals.
    finally:
        if "choice" in locals():
            if choice == "yes":
                clear()
                print(f"WARNING, this WILL overwrite all your files in {full_path}")
                print("There is no way to return your files")
                print("They will not be in the bin, or anywhere, they will be gone..")
                print("Type exactly: Understood, OVERWRITE my folder")
                x = input()
                clear()
                if x == "Understood, OVERWRITE my folder":
                    shutil.rmtree(full_path)
                    mkdir(full_path)
                    print("Your folder has been overwritten.")
        # TODO: Sort out these continuing prints.
                else:
                    print("Continuing without overwriting.")
            else:
                print("Continuing without overwriting.")




def use_folder(full_path, folder, openyn, URL, sys_name):
    """Uses the newly created folder to create a new virtual environment, a .gitignore and a README.md
    If a --open is specified it will attempt to open the IDE at the end.
    If a --url is specified it will attempt to link to that repo."""

    print(f"Do you want to continue and use the {folder}")
    print("Yes / No")
    x = input().lower()
    if x!="yes":
        sys.exit()    
    chdir(full_path)
    if not URL == None:
        system("git init -b main")
        system(f"git remote add origin {URL}")
        system("git remote -v")
    system("echo readme > README.md")
    system(f"echo .{folder} > .gitignore")
    if not URL == None:
        system("git add . && git commit -m 'initial commit'")
        system("git push -u origin main")
    system(f"{'python' if sys_name=='Windows' else 'python3'} -m venv .{folder}")
    if openyn:
        if openyn.lower() in ('code','vsc','vscode'):
            system("code .")
        elif openyn.lower() in ('pycharm','pc'):
            system("pycharm .")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup new project folder")
    parser.add_argument("--f", dest="folder", type=str, help="name of folder to be added")
    parser.add_argument("--open", dest='openyn', default=False, help="To open VScode/Pycharm when done via 'code/pycharm .'")
    parser.add_argument("--url", dest="URL", type=str, help="Use --url URL to provide github url to link to")
    
    args=parser.parse_args()

    folder = args.folder
    URL = args.URL
    openyn = args.openyn

    sys_name = platform.system()
    dir_path = dirname(realpath(__file__))
    full_path = join(dir_path, folder)


    clear()
    print(f"Trying to create >{folder}< in {dir_path}")
    create_folder(full_path)
    use_folder(full_path, folder, openyn, URL, sys_name)
