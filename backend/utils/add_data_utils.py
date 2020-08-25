import csv
import os

from backend.models.group import Group
from backend.utils.get_path_utils import get_group_data_dir, get_group_data_file_path, get_members_data_file_path
from backend.utils.get_path_utils import get_periodic_flow_data_file_path, get_flow_data_file_path
from backend.models.flow import Flow
from backend.models.periodic_flow import PeriodicFlow
from backend.models.member import Member


def add_group_data(group: Group):
    data_path = get_group_data_file_path()
    # Determine if file will be opened with "append" or "write", depending if file already exists or not.
    open_mode = _get_open_mode(data_path)

    # Create group database directory and files.
    group_dir_path = get_group_data_dir(group.name)
    if not os.path.exists(group_dir_path):
        os.makedirs(group_dir_path)
    members_file_path = get_members_data_file_path(group.name)
    if not os.path.exists(members_file_path):
        os.mknod(members_file_path)
    periodic_flows_file_path = get_periodic_flow_data_file_path(group.name)
    if not os.path.exists(periodic_flows_file_path):
        os.mknod(periodic_flows_file_path)
    flows_file_path = get_flow_data_file_path(group.name)
    if not os.path.exists(flows_file_path):
        os.mknod(flows_file_path)

    # Edit file (writing or appending)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(group.to_database())


def add_flow_data(flow: Flow, group_name: str):
    data_path = get_flow_data_file_path(group_name)
    # Determine if file will be opened with "append" or "write", depending if file already exists or not.
    open_mode = _get_open_mode(data_path)
    # Edit file (writing or appending)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(flow.to_database())


def add_periodic_flow_data(periodic_flow: PeriodicFlow, group_name: str):
    data_path = get_periodic_flow_data_file_path(group_name)
    # Determine if file will be opened with "append" or "write", depending if file already exists or not.
    open_mode = _get_open_mode(data_path)
    # Edit file (writing or appending)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file, delimiter='\t')
        writer.writerow(periodic_flow.to_database())


def add_member_data(member: Member, group_name: str):
    data_path = get_members_data_file_path(group_name)
    # Determine if file will be opened with "append" or "write", depending if file already exists or not.
    open_mode = _get_open_mode(data_path)
    # Edit file (writing or appending)
    with open(data_path, open_mode) as data_file:
        writer = csv.writer(data_file)
        writer.writerow(member.to_database())


def _get_open_mode(data_path: str) -> str:
    if os.path.exists(data_path):
        return 'a'
    else:
        return 'w'
