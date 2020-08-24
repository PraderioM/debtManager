import csv

from backend.models.group import Group
from backend.utils.get_path_utils import *
from backend.models.flow import Flow
from backend.models.periodic_flow import PeriodicFlow
from backend.models.member import Member


def add_group_data(group: Group):
    data_path = get_group_data_file_path()
    open_mode = _get_open_mode(data_path)
    os.makedirs(get_group_data_dir(group.name), exist_ok=True)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(group.to_database())


def add_flow_data(flow: Flow, group_name: str):
    data_path = get_flow_data_file_path(group_name)
    open_mode = _get_open_mode(data_path)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(flow.to_database())


def add_periodic_flow_data(periodic_flow: PeriodicFlow, group_name: str):
    data_path = get_periodic_flow_data_file_path(group_name)
    open_mode = _get_open_mode(data_path)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file, delimiter='\t')
        writer.writerow(periodic_flow.to_database())


def add_member_data(member: Member, group_name: str):
    data_path = get_members_data_file_path(group_name)
    open_mode = _get_open_mode(data_path)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(member.to_database())


def _get_open_mode(data_path: str) -> str:
    if os.path.exists(data_path):
        return 'a'
    else:
        return 'w'
