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
        flux_to_database = []
        issuer_name = str(self.issuer[0])
        flux_to_database.append(issuer)
        receiver_name = str(self.receiver[0])
        flux_to_database.append(receiver)
        amount = str(self.amount)
        flux_to_database.append(amount)
        concept = str(self.concept)
        flux_to_database.append(concept)
        date = str(self.date)
        flux_to_database.append(date)
        return flux_to_database


