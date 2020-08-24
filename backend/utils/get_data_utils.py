import csv
from typing import List

from .get_path_utils import get_group_data_file_path, get_members_data_file_path
from .get_path_utils import get_periodic_flow_data_file_path, get_flow_data_file_path
from backend.models.group import Group
from backend.models.member import Member
from backend.models.periodic_flow import PeriodicFlow
from backend.models.flow import Flow


def get_groups_data() -> List[Group]:
    group_list: List[Group] = []
    with open(get_group_data_file_path(), 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:
                continue
            group_list.append(Group.from_database(row))

    return group_list


def get_members_data(group_name: str) -> List[Member]:
    member_list: List[Member] = []

    with open(get_members_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:
                continue
            member_list.append(Member.from_database(row))

    return member_list


def get_periodic_flow_data(group_name: str) -> List[PeriodicFlow]:
    member_list = get_members_data(group_name)

    periodic_flow_list: List[PeriodicFlow] = []
    with open(get_periodic_flow_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file, delimiter='\t')
        for row in reader:
            if len(row) == 0:
                continue

            periodic_flow_list.append(PeriodicFlow.from_database(row, member_list=member_list))

    return periodic_flow_list


def get_flow_data(group_name: str) -> List[Flow]:
    flow_list: List[Flow] = []
    member_list = get_members_data(group_name)

    with open(get_flow_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:
                continue
            flow_list.append(Flow.from_database(row, member_list=member_list))
    return flow_list
