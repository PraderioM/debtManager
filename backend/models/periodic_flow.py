from datetime import date
import json
from typing import Dict, List, Optional, Tuple, Union

from backend.models.flow import Flow
from backend.models.member import Member
from backend.models.typing_hints import Burden
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

    @classmethod
    def from_frontend(cls, frontend_data: Dict):
        receiver_list = [
            (Member.from_frontend(receiver_dict['receiver']), receiver_dict['burden'])
            for receiver_dict in frontend_data['receiverList']
        ]
        return PeriodicFlow(amount_payed=frontend_data['amountPayed'],
                            period=frontend_data['period'],
                            pay_day=frontend_data['payDay'],
                            last_payed=date_from_iso_format(frontend_data['lastPayed']),
                            issuer=Member.from_frontend(frontend_data['issuer']),
                            receiver_list=receiver_list,
                            is_update_automatic=frontend_data['isUpdateAutomatic'])

    def to_database(self) -> List[str]:
        return [str(self.amount_payed), str(self.period), str(self.pay_day), str(self.last_payed), self.issuer.name,
                str(self.receiver_list), str(self.is_update_automatic)]

    def to_frontend(self) -> Dict:
        return {
            'amountPayed': self.amount_payed,
            'period': self.period,
            'payDay': self.pay_day,
            'lastPayed': str(self.last_payed),
            'issuer': self.issuer.to_frontend(),
            'receiverList': [
                {
                    'receiver': receiver.to_frontend(),
                    'burden': burden
                }
                for receiver, burden in self.receiver_list
            ],
            'isUpdateAutomatic': self.is_update_automatic
        }

    def generate_periodic_flows(self) -> List[Flow]:
        # Todo implement.
        pass

    @property
    def is_amount_fixed(self) -> bool:
        return self.amount_payed is not None
