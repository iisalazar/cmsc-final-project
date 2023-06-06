from dataclasses import dataclass


@dataclass
class Transaction:
    id: int
    name: str
    amount: int
    dateCreated: str
    personId: int
    grpId: int
    lenderId: int
    lendeeId: int
    type: str
