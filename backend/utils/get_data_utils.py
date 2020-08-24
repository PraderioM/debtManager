import csv
import datetime
from typing import List, Optional

from .get_path_utils import get_group_data_file_path, get_members_data_file_path
from .get_path_utils import get_periodic_flux_data_file_path, get_flux_data_file_path
from backend.models.group import Group
from backend.models.member import Member
from backend.models.periodic_flux import PeriodicFlux
from backend.models.flux import Flux


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


def get_periodic_flux_data(group_name: str) -> List[PeriodicFlux]:
    member_list = get_members_data(group_name)

    periodic_flux_list: List[PeriodicFlux] = []
    with open(get_periodic_flux_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file, delimiter='\t')
        for row in reader:
            if len(row) == 0:
                continue

            periodic_flux_list.append(PeriodicFlux.from_database(row, member_list=member_list))

    return periodic_flux_list


def get_flux_data(group_name: str, date: Optional[datetime.date] = None) -> List[Flux]:
    flux_list: List[Flux] = []
    member_list = get_members_data(group_name)

    with open(get_flux_data_file_path(group_name, date=date), 'r') as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            if len(row) == 0:
                continue

            flux_list.append(Flux.from_database(row, member_list=member_list))

    return flux_list
