import os
from pathlib import Path


project_name = " us_visa"

List_of_files = [

    f"{project_name}/__init__.py",   #constructor ( like starting initialization)
    f"{project_name}/components/__init__py",    # path
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]

for filepath in List_of_files:                #  List_of_file [ all lists of Path ] passing to filepath
    filepath = Path(filepath)                   # import - > Path is to using here to detect Os MAchine for to find / \ , like WindowsPath
    
    filedir, filename = os.path.split(filepath)   # foldername, filename = os.path.split( listed of paths ) o/p " utils", "utils.py "

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")