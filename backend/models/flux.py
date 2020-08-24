from datetime import datetime
from typing import Optional

from .member import Member


class Flux:
    def __init__(self, issuer: Member, receiver: Member, amount: float, concept: str, date: Optional[datetime]):
        self.issuer = issuer
        self.receiver = receiver
        self.amount = amount
        self.concept = concept
        self.date = datetime.now() if date is None else date
