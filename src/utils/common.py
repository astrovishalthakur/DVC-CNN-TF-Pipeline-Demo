import os
import yaml
import logging
from tqdm import tqdm
import json
import shutil
import time

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

    N = len(list_of_files)

    for filename in tqdm(
        list_of_files,
        total=N,
        desc=f"copying file from {source_data_dir} to {local_data_dir}",
        colour="green",
        ):
        src = os.path.join(source_data_dir, filename)
        dest = os.path.join(local_data_dir, filename)
        shutil.copy(src, dest)


    logging.info(
        f"all the files has been copied from {source_data_dir} to {local_data_dir}"
    )


def get_timestamp(name:str) -> str:
    timestamp = time.asctime().replace(" ",'_').replace(":",".")
    unique_name = f"{name}_at_{timestamp}"
    return unique_name