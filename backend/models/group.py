from typing import Dict, List


class Group:
    def __init__(self, name: str, mailgun_1: str, mailgun_2: str):
        self.name = name
        self.mailgun_1 = mailgun_1
        self.mailgun_2 = mailgun_2

    @classmethod
    def from_database(cls, database_data: List[str]) -> 'Group':
        name, mailgun_1, mailgun_2 = database_data
        return Group(name=name, mailgun_1=mailgun_1, mailgun_2=mailgun_2)

    @classmethod
    def from_frontend(cls, frontend_data: Dict[str, str]):
        return Group(name=frontend_data['name'],
                     mailgun_1=frontend_data['mailgun1'],
                     mailgun_2=frontend_data['mailgun2'])

    def to_database(self) -> List[str]:
        return [self.name, self.mailgun_1, self.mailgun_2]

    def to_frontend(self) -> Dict[str, str]:
        return {'name': self.name, 'mailgun1': self.mailgun_1, 'mailgun2': self.mailgun_2}
