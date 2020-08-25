import csv
from glob import glob
import os

from backend.utils.get_data_utils import get_groups_data, get_flow_data, get_members_data, get_periodic_flow_data
from backend.utils.get_path_utils import get_group_data_file_path, get_group_data_dir, get_flow_data_file_path, \
    get_members_data_file_path, get_periodic_flow_data_file_path


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


def remove_flow_data(group_name: str, id_: int):
    # Get list of all flows and remove the one in specified position.

    flow_list = get_flow_data(group_name)
    flow_list.pop(id_)

    # re-write all flows in database except the removed one.
    with open(get_flow_data_file_path(group_name), 'w') as data_file:
        writer = csv.writer(data_file)
        for flow in flow_list:
            writer.writerow(flow.to_database())


def remove_members_data(group_name: str, id_: int):
    # Get list of all members and remove the one in specified position.

    members_list = get_members_data(group_name)
    members_list.pop(id_)

    # re-write all members in database except the removed one.
    with open(get_members_data_file_path(group_name), 'w') as data_file:
        writer = csv.writer(data_file)
        for member in members_list:
            writer.writerow(member.to_database())


def remove_periodic_flow_data(group_name: str, id_: int):
    # Get list of all periodic flows and remove the one in specified position.

    periodic_flow_list = get_periodic_flow_data(group_name)
    periodic_flow_list.pop(id_)

    # Re-write all periodic flows in database except the removed one.
    with open(get_periodic_flow_data_file_path(group_name), 'w') as data_file:
        writer = csv.writer(data_file)
        for periodic_flow in periodic_flow_list:
            writer.writerow(periodic_flow.to_database())
