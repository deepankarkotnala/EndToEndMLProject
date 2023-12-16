'''
This file is used to manually generate a project directory structure. 
Automatically bhi hota hai using some tool ... cookiecutter

This will be a generic code and isme bas project name change kar do, 
and the new ML project's structure will be ready
'''

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

# ye sab files/folders ban jayenge 
## __init__.py file jis folder ke andar banegi, uska package ban jayega when we compile the code (run setup file)

list_of_files = [
  #  ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py", 
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
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