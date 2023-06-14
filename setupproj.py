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
    print(f""".{folder} 
           
# Created by https://www.toptal.com/developers/gitignore/api/macos
# Edit at https://www.toptal.com/developers/gitignore?templates=macos

### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### macOS Patch ###
# iCloud generated files
*.icloud

# End of https://www.toptal.com/developers/gitignore/api/macos

# added from github:

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/""", 
file=".gitignore")
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
