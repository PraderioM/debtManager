from typing import List, Optional, Tuple

from .flux import Flux
from . member import Member
from .typing_hints import Burden


class PeriodicFlux:
    def __init__(self, amount_payed: Optional[float], period: int, pay_day: int, issuer: Member,
                 receiver_list: List[Tuple[Member, Burden]]):
        self.amount_payed = amount_payed
        self.period = period
        self.pay_day = pay_day
        self.issuer = issuer
        self.receiver_list = receiver_list

    def generate_fluxes(self) -> List[Flux]:
        # todo implement.
        pass

    @property
    def is_amount_fixed(self) -> bool:
        return self.amount_payed is not None
