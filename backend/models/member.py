from typing import List, Optional


class Member:
    def __init__(self, name: str, e_mail: Optional[str],
                 creditor_threshold: float = 100,
                 debtor_threshold: float = 100):
        self.name = name
        self._e_mail = e_mail
        self.creditor_threshold = creditor_threshold
        self.debtor_threshold = debtor_threshold

    @classmethod
    def from_database(cls, database_data: List[str]) -> 'Member':
        name, e_mail, creditor_threshold, debtor_threshold = database_data
        return Member(name=name,
                      e_mail=e_mail,
                      creditor_threshold=float(creditor_threshold),
                      debtor_threshold=float(debtor_threshold))

    def to_database(self) -> List[str]:
        return [self.name, self.e_mail, str(self.creditor_threshold), str(self.debtor_threshold)]
