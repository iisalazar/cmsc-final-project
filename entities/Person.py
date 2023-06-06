from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Person:
    id: int
    name: str
    is_user: bool
