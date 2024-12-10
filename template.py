import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project Name
project_name = "Cardio_care"

# Updated list of files for the project structure
list_of_files = [
    ".github/workflows/.gitkeep",                        # GitHub Actions folder
    f"src/{project_name}/__init__.py",                   # Project package init
    f"src/{project_name}/components/__init__.py",        # Components module
    f"src/{project_name}/utils/__init__.py",             # Utils module
    f"src/{project_name}/utils/common.py",               # Common utilities
    f"src/{project_name}/config/__init__.py",            # Config package
    f"src/{project_name}/config/configuration.py",       # Configuration module
    f"src/{project_name}/pipeline/__init__.py",          # Pipeline package
    f"src/{project_name}/pipeline/train_pipeline.py",    # Training pipeline
    f"src/{project_name}/entity/__init__.py",            # Entity module
    f"src/{project_name}/entity/config_entity.py",       # Config entity
    f"src/{project_name}/constants/__init__.py",         # Constants module
    "config/config.yaml",                                # Configuration file
    "params.yaml",                                       # Parameters file
    "schema.yaml",                                       # Data schema
    "main.py",                                           # Main execution script
    "Dockerfile",                                        # Docker configuration
    "setup.py",                                          # Package setup
    "notebook/EDA.ipynb",
    "notebook/model.ipynb",                                                      # Research notebook
    "data/raw/.gitkeep",                                 # Folder for raw data
    "data/processed/.gitkeep",                           # Folder for processed data
    "app.py",                                            # FastAPI app
]

# Iterate through files to create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create files if they don't exist or are empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

# Inform the user that the structure is complete
logging.info("Project structure created successfully!")
