class Member:
    def __init__(self, name: str, e_mail: str, creditor_threshold: float, debtor_threshold: float):
        self.name = name
        self._e_mail = e_mail
        self.creditor_threshold = creditor_threshold
        self.debtor_threshold = debtor_threshold
