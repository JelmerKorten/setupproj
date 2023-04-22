
# (or echo .VENVNAME > .gitignore)

# inputs:
# main.py folder github-url open

import sys
from os import system, mkdir, makedirs, chdir
from os.path import dirname, realpath, join
import platform
import shutil
import argparse


# sys.argv[] where 0 is the name of the program:
# print("program name:\t",sys.argv[0])
# Check if folder exists
# print(platform.system()) # windows has python
# folder = sys.argv[1]
# new_folder = folder[folder.rfind("/"):]
# old_dir = folder[:folder.rfind("/")]

clear = lambda: system("cls || clear")

def create_folder(full_path):
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
                else:
                    print("Continuing without overwriting.")
            else:
                print("Continuing without overwriting.")




def use_folder(full_path, folder, openyn, URL, sys_name):
    print(f"Do you want to continue and use the {folder}")
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
    parser.add_argument("--open", dest='openyn', default=False, help="To open VScode when done via 'code .'")
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
