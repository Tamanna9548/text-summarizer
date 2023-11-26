import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"



list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",           #constructor file{__init__.py}:to do import operation need to install this as local package
    f"src/{project_name}/conponents/__init__.py",  #folder name components again one constructor file
    f"src/{project_name}/utils/__init__.py",   #folder utils to put util related code
    f"src/{project_name}/utils/common.py",    #common ke andr utility honge sare
    f"src/{project_name}/logging/__init__.py",  #loggin folder with constructor file
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", #another folder pipeline this will contain about trading and pridiction pipeline 
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",  #here we keep all model related parameter
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "text.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")