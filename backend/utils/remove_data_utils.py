import csv
from glob import glob
import os

from backend.utils.get_path_utils import get_group_data_dir, get_group_data_file_path
from backend.utils.get_data_utils import get_groups_data


def remove_group_data(id_: int):
    # Get a list of all groups and remove group at index id_.
    group_list = get_groups_data()
    group = group_list.pop(id_)

    # Updating group database in order to remove group.
    with open(get_group_data_file_path(), 'w') as data_file:
        writer = csv.writer(data_file)
        for group in group_list:
            writer.writerow(group.to_database())

    # Removing all database files in group sub-filder.
    group_dir = get_group_data_dir(group.name)
    for file_path in glob(os.path.join(group_dir, '*')):
        os.remove(file_path)

    # Removing group sub-folder.
    os.rmdir(group_dir)


# Todo other 3 removes (flows, members and periodical_flos)