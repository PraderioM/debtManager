import datetime

from typing import List

from backend.models.member import Member


def get_member_by_name(name: str, member_list: List[Member]) -> Member:
    for member in member_list:
        if name == member.name:
            return member

    return Member(name=name, e_mail=None)


def date_from_iso_format(iso_format_date: str) -> datetime.date:
    year, month, day = iso_format_date.split('-')
    return datetime.date(int(year), int(month), int(day))


def datetime_from_iso_format(iso_format_date: str) -> datetime.datetime:
    date, time = iso_format_date.split(' ')
    year, month, day = date.split('-')
    hour, minute, second = time.split(':')
    second, microsecond = second.split('.')
    return datetime.datetime(year=int(year), month=int(month), day=int(day), hour=int(hour),
                             minute=int(minute), second=int(second), microsecond=int(microsecond))



