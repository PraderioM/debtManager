import os

from backend.constants import DATA_DIR_PATH, GROUP_DATA_FILE_NAME, MEMBERS_DATA_FILE_NAME
from backend.constants import PERIODIC_FLOW_DATA_FILE_NAME, FLOW_DATA_FILE_NAME


def get_group_data_file_path() -> str:
    return os.path.join(DATA_DIR_PATH, GROUP_DATA_FILE_NAME)


def get_group_data_dir(group_name: str) -> str:
    return os.path.join(DATA_DIR_PATH, group_name.replace(' ', '-'))


def get_members_data_file_path(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), MEMBERS_DATA_FILE_NAME)


def get_periodic_flow_data_file_path(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), PERIODIC_FLOW_DATA_FILE_NAME)


def get_flow_data_file_path(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), FLOW_DATA_FILE_NAME)
