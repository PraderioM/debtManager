import datetime
import os
from glob import glob
from typing import List, Optional

from backend.constants import DATA_DIR_PATH, GROUP_DATA_FILE_NAME, MEMBERS_DATA_FILE_NAME, PERIODIC_FLUX_DATA_FILE_NAME, \
    FLUX_DATA_DIR_NAME


def get_group_data_file_path() -> str:
    return os.path.join(DATA_DIR_PATH, GROUP_DATA_FILE_NAME)


def get_group_data_dir(group_name: str) -> str:
    return os.path.join(DATA_DIR_PATH, group_name.replace(' ', '-'))


def get_members_data_file_path(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), MEMBERS_DATA_FILE_NAME)


def get_periodic_flux_data_file_path(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), PERIODIC_FLUX_DATA_FILE_NAME)


def get_flux_data_dir(group_name: str) -> str:
    return os.path.join(get_group_data_dir(group_name), FLUX_DATA_DIR_NAME)


def get_all_flux_data_file_paths(group_name: str) -> List[str]:
    return sorted(list(glob(os.path.join(get_flux_data_dir(group_name), '*'))))


def get_flux_data_file_path(group_name: str, date: Optional[datetime.date] = None) -> str:
    if date is None:
        return get_all_flux_data_file_paths(group_name)[-1]
    else:
        return os.path.join(get_flux_data_dir(group_name), str(date) + '.csv')
