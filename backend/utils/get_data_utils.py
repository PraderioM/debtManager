import csv
import datetime
import json
from typing import List, Optional

from backend.constants import NONE_STRING, TRUE_STRING
from .get_path_utils import get_group_data_file_path, get_members_data_file_path
from .get_path_utils import get_periodic_flux_data_file_path, get_flux_data_file_path
from backend.models.group import Group
from backend.models.member import Member
from backend.models.periodic_flux import PeriodicFlux
from backend.models.flux import Flux
from backend.utils.utils import get_member_by_name, date_from_iso_format


def get_groups_data() -> List[Group]:
    group_list: List[Group] = []
    with open(get_group_data_file_path(), 'r') as data_file:
        reader = csv.reader(data_file)
        for group_name, mailgun_1, mailgun_2 in reader:
            group_list.append(Group(name=group_name, mailgun_1=mailgun_1, mailgun_2=mailgun_2))

    return group_list


def get_members_data(group_name: str) -> List[Member]:
    member_list: List[Member] = []

    with open(get_members_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file)
        for name, e_mail, creditor_threshold, debtor_threshold in reader:
            member_list.append(Member(name=name,
                                      e_mail=e_mail,
                                      creditor_threshold=float(creditor_threshold),
                                      debtor_threshold=float(debtor_threshold)))

    return member_list


def get_periodic_flux_data(group_name: str) -> List[PeriodicFlux]:
    member_list = get_members_data(group_name)

    periodic_flux_list: List[PeriodicFlux] = []
    with open(get_periodic_flux_data_file_path(group_name), 'r') as data_file:
        reader = csv.reader(data_file, delimiter='\t')
        for amount_payed, period, pay_day, last_payed, issuer_name, receiver_list_data, is_update_automatic in reader:
            amount_payed = None if amount_payed == NONE_STRING else float(amount_payed)
            is_update_automatic = True if is_update_automatic == TRUE_STRING else False
            issuer = get_member_by_name(issuer_name, member_list)
            receiver_list = [
                (get_member_by_name(receiver_name, member_list), float(burden))
                for receiver_name, burden in json.loads(receiver_list_data)
            ]
            periodic_flux_list.append(PeriodicFlux(amount_payed=amount_payed,
                                                   period=int(period),
                                                   pay_day=int(pay_day),
                                                   last_payed=date_from_iso_format(last_payed),
                                                   issuer=issuer,
                                                   receiver_list=receiver_list,
                                                   is_update_automatic=is_update_automatic))

    return periodic_flux_list


def get_flux_data(group_name: str, date: Optional[datetime.date] = None) -> List[Flux]:
    flux_list: List[Flux] = []
    member_list = get_members_data(group_name)

    with open(get_flux_data_file_path(group_name, date=date), 'r') as data_file:
        reader = csv.reader(data_file)
        for issuer_name, receiver_name, amount, concept, date in reader:
            flux_list.append(Flux(issuer=get_member_by_name(issuer_name, member_list),
                                  receiver=get_member_by_name(receiver_name, member_list),
                                  amount=float(amount),
                                  concept=concept,
                                  date=date_from_iso_format(date)))

    return flux_list
