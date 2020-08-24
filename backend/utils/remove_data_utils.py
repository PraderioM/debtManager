import csv
from glob import glob
import os

from backend.utils.get_data_utils import get_groups_data
from backend.utils.get_path_utils import get_group_data_file_path, get_group_data_dir


def remove_group_data(id_: int):
    # Get list of all groups and remove the one in specified position.
    group_list = get_groups_data()
    removed_group = group_list.pop(id_)

    # re-write all groups in database except the removed one.
    with open(get_group_data_file_path(), 'w') as data_file:
        writer = csv.writer(data_file)
        for group in group_list:
            writer.writerow(group.to_database())

    # Remove all database files corresponding to removed group.
    group_dir_path = get_group_data_dir(removed_group.name)
    for file_path in glob(os.path.join(group_dir_path, '*')):
        os.remove(file_path)

    # Remove now empty directory.
    os.rmdir(group_dir_path)
