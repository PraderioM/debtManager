from typing import Dict, List, Optional, Union

from aiohttp import web


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

    @classmethod
    def from_frontend(cls, frontend_data: Dict[str, Union[str, float]]) -> 'Member':
        return Member(name=frontend_data['name'],
                      e_mail=frontend_data['eMail'],
                      creditor_threshold=frontend_data['creditor_threshold'],
                      debtor_threshold=frontend_data['debtor_threshold'])

    @classmethod
    def pre_process_request(cls, request: web.Request) -> Dict:
        return {
            'name': request.rel_url.query['name'],
            'e_mail': request.rel_url.query['e_mail'],
            'creditor_threshold': float(request.rel_url.query['creditor_threshold']),
            'debtor_threshold': float(request.rel_url.query['debtor_threshold']),
        }

    def to_database(self) -> List[str]:
        return [self.name, self.e_mail, str(self.creditor_threshold), str(self.debtor_threshold)]

    def to_frontend(self) -> Dict[str, Union[str, float]]:
        return {
            'name': self.name,
            'eMail': self.e_mail,
            'creditorThreshold': self.creditor_threshold,
            'debtorThreshold': self.debtor_threshold
        }

    @property
    def e_mail(self) -> str:
        if self._e_mail is None:
            return ''
        else:
            return self._e_mail
