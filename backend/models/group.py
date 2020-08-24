from typing import List


class Group:
    def __init__(self, name: str, mailgun_1: str, mailgun_2: str):
        self.name = name

    @classmethod
    def from_database(cls, database_data: List[str]) -> 'Group':
        name, mailgun_1, mailgun_2 = database_data
        return Group(name=name, mailgun_1=mailgun_1, mailgun_2=mailgun_2)
