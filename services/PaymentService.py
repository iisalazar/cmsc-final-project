from services.TransactionService import TransactionService, UpdateTransactionDto
from db import db
from dataclasses import dataclass
from typing import List
from entities.Transaction import Transaction


@dataclass
class CreatePaymentDto:
    amount: int
    name: str
    date: str


@dataclass
class CreateFriendPaymentDto(CreatePaymentDto):
    person_id: int
    lender_id: int
    lendee_id: int


@dataclass
class CreateGroupPaymentDto(CreatePaymentDto):
    grp_id: int
    lender_id: int
    lendee_id: int


class PaymentService(TransactionService):
    def __init__(self):
        super().__init__()

    def create_friend_payment(self, payment: CreateFriendPaymentDto) -> Transaction:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO transaction (name, amount, personId, grpId, lenderId, lendeeId, type, dateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())",
            (
                payment.name,
                payment.amount,
                payment.person_id,
                None,
                payment.lender_id,
                payment.lendee_id,
                "payment",
            ),
        )
        db.commit()

        cursor.close()
        return Transaction(
            cursor.lastrowid,
            payment.name,
            payment.amount,
            None,
            payment.person_id,
            None,
            payment.lender_id,
            payment.lendee_id,
            "payment",
        )

    def create_group_payment(self, payment: CreateGroupPaymentDto) -> Transaction:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO transaction (name, amount, personId, grpId, lenderId, lendeeId, type, dateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())",
            (
                payment.name,
                payment.amount,
                None,
                payment.grp_id,
                payment.lender_id,
                payment.lendee_id,
                "payment",
            ),
        )
        db.commit()

        cursor.close()
        return Transaction(
            cursor.lastrowid,
            payment.name,
            payment.amount,
            None,
            None,
            payment.grp_id,
            payment.lender_id,
            None,
            "payment",
        )

    def update_payment(
        self, payment_id: int, payment: UpdateTransactionDto
    ) -> Transaction:
        self.update_transaction(payment_id, payment)

    def delete_payment(self, payment_id: int) -> None:
        self.delete_transaction(payment_id)
