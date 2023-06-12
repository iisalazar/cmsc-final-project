from services.TransactionService import TransactionService, UpdateTransactionDto
from db import db
from dataclasses import dataclass
from typing import List
from entities.Transaction import Transaction


@dataclass
class CreatePaymentDto:
    amount: int
    name: str


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
            payment.lendee_id,
            "payment",
        )

    def update_payment(
        self, payment_id: int, payment: UpdateTransactionDto
    ) -> Transaction:
        self.update_transaction(payment_id, payment, type="payment")

    def delete_payment(self, payment_id: int) -> None:
        self.delete_transaction(payment_id, "payment")

    def view_payments(self, person_id: int) -> List[Transaction]:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM transaction WHERE personId = %s AND type = 'payment'",
            (person_id,),
        )
        results = cursor.fetchall()
        payments: List[Transaction] = []

        for result in results:
            payments.append(
                Transaction(
                    result[0],
                    result[1],
                    result[2],
                    result[3],
                    result[4],
                    result[5],
                    result[6],
                    result[7],
                    result[8],
                )
            )
        cursor.close()
        return payments

    def get_payment(self, payment_id: int) -> Transaction | None:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM transaction WHERE id = %s AND type = 'payment'",
            (payment_id,),
        )
        result = cursor.fetchone()
        if result is None:
            return None
        cursor.close()
        return Transaction(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8],
        )
