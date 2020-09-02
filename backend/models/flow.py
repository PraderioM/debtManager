from aiohttp import web
import datetime
from typing import Dict, List, Optional


from backend.models.member import Member
from backend.utils.utils import date_from_iso_format, get_member_by_name


class Flow:
    def __init__(self, issuer: Member, receiver: Member, amount: float, concept: str,
                 date: Optional[datetime.date] = None):
        self.issuer = issuer
        self.receiver = receiver
        self.amount = amount
        self.concept = concept
        self.date = datetime.date.today() if date is None else date

    @classmethod
    def from_database(cls, database_data: List[str], member_list: List[Member]) -> 'Flow':
        issuer_name, receiver_name, amount, concept, date = database_data
        return Flow(issuer=get_member_by_name(issuer_name, member_list),
                    receiver=get_member_by_name(receiver_name, member_list),
                    amount=float(amount),
                    concept=concept,
                    date=date_from_iso_format(date))

    @classmethod
    def from_frontend(cls, frontend_data: Dict) -> 'Flow':
        return Flow(issuer=Member.from_frontend(frontend_data['issuer']),
                    receiver=Member.from_frontend(frontend_data['receiver']),
                    amount=frontend_data['amount'],
                    concept=frontend_data['concept'],
                    date=date_from_iso_format(frontend_data['date']))

    @classmethod
    def pre_process_request(cls, request: web.Request) -> Dict:
        return {
            'issuer': request.rel_url.query['issuer'],
            'receiver': request.rel_url.query['receiver'],
            'amount': float(request.rel_url.query['amount']),
            'concept': request.rel_url.query['concept'],
            'date': request.rel_url.query['date']
        }

    def to_database(self) -> List[str]:
        return [self.issuer.name, self.receiver.name, str(self.amount), self.concept, str(self.date)]

    def to_frontend(self) -> Dict:
        return {
            'issuer': self.issuer.to_frontend(),
            'receiver': self.receiver.to_frontend(),
            'amount': self.amount,
            'concept': self.concept,
            'date': str(self.date),
        }
