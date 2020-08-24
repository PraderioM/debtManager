from datetime import date
import json
from typing import List, Optional, Tuple

from .flow import Flow
from .member import Member
from .typing_hints import Burden
from backend.constants import NONE_STRING, TRUE_STRING
from backend.utils.utils import date_from_iso_format, get_member_by_name


class PeriodicFlow:
    def __init__(self, amount_payed: Optional[float],
                 period: int, pay_day: int, last_payed: date,
                 issuer: Member,
                 receiver_list: List[Tuple[Member, Burden]],
                 is_update_automatic: bool):
        self.amount_payed = amount_payed
        self.period = period
        self.pay_day = pay_day
        self.last_payed = last_payed
        self.issuer = issuer
        self.receiver_list = receiver_list
        self.is_update_automatic = is_update_automatic

    @classmethod
    def from_database(cls, database_data: List[str], member_list: List[Member]) -> 'PeriodicFlow':
        amount_payed, period, pay_day, last_payed, issuer_name, receiver_list_data, is_update_automatic = database_data
        amount_payed = None if amount_payed == NONE_STRING else float(amount_payed)
        is_update_automatic = True if is_update_automatic == TRUE_STRING else False
        issuer = get_member_by_name(issuer_name, member_list)
        receiver_list = [
            (get_member_by_name(receiver_name, member_list), float(burden))
            for receiver_name, burden in json.loads(receiver_list_data)
        ]
        return PeriodicFlow(amount_payed=amount_payed,
                            period=int(period),
                            pay_day=int(pay_day),
                            last_payed=date_from_iso_format(last_payed),
                            issuer=issuer,
                            receiver_list=receiver_list,
                            is_update_automatic=is_update_automatic)

    def to_database(self) -> List[str]:
        return [str(self.amount_payed), str(self.period), str(self.pay_day), str(self.last_payed), self.issuer.name,
                str(self.receiver_list), str(self.is_update_automatic)]


    def generate_fluxes(self) -> List[Flow]:
        # todo implement.
        pass

    @property
    def is_amount_fixed(self) -> bool:
        return self.amount_payed is not None
