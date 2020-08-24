import datetime
from typing import List, Optional

from .member import Member
from backend.utils.utils import date_from_iso_format, get_member_by_name


class Flux:
    def __init__(self, issuer: Member, receiver: Member, amount: float, concept: str, date: Optional[datetime.date]):
        self.issuer = issuer
        self.receiver = receiver
        self.amount = amount
        self.concept = concept
        self.date = datetime.date.today() if date is None else date

    @classmethod
    def from_database(cls, database_data: List[str], member_list: List[Member]) -> 'Flux':
        issuer_name, receiver_name, amount, concept, date = database_data
        return Flux(issuer=get_member_by_name(issuer_name, member_list),
                    receiver=get_member_by_name(receiver_name, member_list),
                    amount=float(amount),
                    concept=concept,
                    date=date_from_iso_format(date))

    def to_database(self) -> List[str]:
        return [self.issuer.name, self.receiver.name, str(self.amount), self.concept, str(self.date)]
