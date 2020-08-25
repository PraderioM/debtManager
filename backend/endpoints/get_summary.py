import json
from typing import Dict, List, Tuple

from aiohttp import web

from backend.models.flow import Flow
from backend.models.member import Member
from backend.utils.get_data_utils import get_flow_data, get_members_data
from backend.utils.utils import get_member_by_name


async def get_summary(request: web.Request) -> web.Response:
    group_name = request.rel_url.query['groupName']

    flow_list = get_compensating_flows(group_name=group_name)

    return web.Response(status=200, body=json.dumps([flow.to_frontend() for flow in flow_list]))


def get_compensating_flows(group_name: str) -> List[Flow]:
    debt_dict: Dict[str, float] = {}
    for flow in get_flow_data(group_name):
        # Reduce debt from the person paying.
        if flow.issuer.name not in debt_dict.keys():
            debt_dict[flow.issuer.name] = 0.
        debt_dict[flow.issuer.name] -= flow.amount

        # Increase debt of the person receiving money.
        if flow.receiver.name not in debt_dict.keys():
            debt_dict[flow.receiver.name] = 0.
        debt_dict[flow.receiver.name] += flow.amount

    # Separate members into people that has payed more than received and vice versa.
    all_members = get_members_data(group_name)
    more_issued: List[Tuple[Member, float]] = []
    more_received: List[Tuple[Member, float]] = []
    for member_name, debt in debt_dict.items():
        member = get_member_by_name(member_name, all_members)
        if debt < 0:
            more_issued.append((member, debt))
        elif debt > 0:
            more_received.append((member, debt))

    # Sort lists in decreasing absolute value of debt.
    more_issued = sorted(more_issued, key=lambda t: t[1])
    more_received = sorted(more_received, key=lambda t: t[1], reverse=True)

    # Create compensating flows by making members of both list pay each other.
    compensating_flows: List[Flow] = []
    while len(more_issued) > 0 and len(more_received) > 0:
        more_issued_member, more_issued_debt = more_issued[0]
        more_received_member, more_received_debt = more_received[0]

        if -more_issued_debt > more_received_debt:
            # If more_received must pay less than what more_issued must receive more_issued_pays everything
            # and is removed from list.
            amount = more_received_debt
            more_issued[0] = more_issued_member, more_issued_debt + more_received_debt
            more_received.pop(0)
        elif -more_issued_debt < more_received_debt:
            # If the situation is the opposite the more_issued member receives all the money it must from the
            # more_received member.
            amount = -more_issued_debt
            more_received[0] = more_received_member, more_issued_debt + more_received_debt
            more_issued.pop(0)
        else:
            # If both debts cancel out we remove issuers from both lists.
            amount = more_received_debt
            more_received.pop(0)
            more_issued.pop(0)

        # Add flow with computed amount:
        compensating_flows.append(Flow(issuer=more_received_member, receiver=more_issued_member,
                                       amount=amount, concept='debt balancing'))

    return compensating_flows
