from typing import Optional


class Member:
    def __init__(self, name: str, e_mail: Optional[str],
                 creditor_threshold: float = 100,
                 debtor_threshold: float = 100):
        self.name = name
        self._e_mail = e_mail
        self.creditor_threshold = creditor_threshold
        self.debtor_threshold = debtor_threshold
