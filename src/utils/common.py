import os
import yaml
import logging
import time
import pandas as pd
import json
import shutil

def read_yaml(path_to_yaml: str) -> dict:
    """it reads yaml file into dictionory
    Args:
        path_to_yaml_file (str): path of the yaml sikh with different agendars
    Returns:
        dict: returns the key-value pair from yaml file
    """
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    """Responsible for creating directories whenerver required
    Args:
        list_of_directories (list): [description]
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


def copy_files(source_data_dir:str, local_data_dir:str) -> None:
    """Copies file from source to destination directory
    Args:
        source_data_dir (str): source data directory
        local_data_dir (str): local data directory
    """
    list_of_files = os.listdir(source_data_dir)

    for file in list_of_files:
        src = os.path.join(source_data_dir, file)
        dest = os.path.join(local_data_dir, file)

        shutil.copy(src, dest)
    logging.info("copy of files successful")