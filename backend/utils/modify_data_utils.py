import csv

from backend.models.group import Group
from backend.models.flow import Flow
from backend.models.periodic_flow import PeriodicFlow
from backend.utils.get_path_utils import *
from backend.utils.get_data_utils import get_groups_data, get_members_data, get_periodic_flow_data, get_flow_data


def modify_group_data(group: Group, id_: int):
    group_list = get_groups_data()
    group_list[id_] = group

    with open(get_group_data_file_path(), 'w') as data_file:
        writer = csv.writer(data_file)
        for group in group_list:
            writer.writerow(group.to_database())


def modify_flow_data(flow: Flow, id_: int, group_name: str):
    flow_list = get_flow_data(group_name)
    flow_list[id_] = flow

    with open(get_flow_data_file_path(group_name), 'w') as data_file:
        writer = csv.writer(data_file)
        for flow in flow_list:
            writer.writerow(flow.to_database())


def modify_periodic_flow_data(periodic_flow: PeriodicFlow, id_: int, group_name: str):
    periodic_flow_list = get_periodic_flow_data(group_name)
    periodic_flow_list[id_] = periodic_flow

    with open(get_periodic_flow_data_file_path(group_name), 'w') as data_file:
        writer = csv.writer(data_file)
        for periodic_flow in periodic_flow_list:
            writer.writerow(periodic_flow.to_database())


def modify_members_data(group: Group, id_: int):
    # Todo
    _list = get_groups_data()
    group_list[id_] = group

    with open(get_group_data_file_path(), 'w') as data_file:
        writer = csv.writer(data_file)
        for group in group_list:
            writer.writerow(group.to_database())

