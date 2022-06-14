import argparse
import os
from numpy import source
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories, copy_files


STAGE = "Get_Data" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def get_data(config_path):
    ## read config files
    """takes path of config files and get data from source directory.
    if  

    Args:
        config_path (str): takes path of config file
    """
    config = read_yaml(config_path)
    source_data_dirs = config['source_data_dirs']
    local_data_dirs = config['local_data_dirs']

    for source_data_dir, local_data_dir in tqdm(
        zip(source_data_dirs, local_data_dirs),
        total=2,
        desc="copying folders.", 
        colour="red"
        ):
        create_directories([local_data_dir])
        copy_files(source_data_dir, local_data_dir)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        get_data(config_path=parsed_args.config, params_path=parsed_args.params)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e