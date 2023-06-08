from db import db
from entities.Transaction import Transaction
from typing import Dict, List
from dataclasses import dataclass


@dataclass
class UpdateTransactionDto:
    name: str
    amount: int


class TransactionService:
    def get_user_transactions(self, id):
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM transaction WHERE transaction.personId = %s", (id,)
        )
        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            t = Transaction(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
            )
            transactions.append(t)

        cursor.close()

        return transactions

    def search_transactions(self, search_term: str) -> List[Transaction]:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM transaction WHERE transaction.name LIKE %s",
            ("%" + search_term + "%",),
        )

        rows = cursor.fetchall()

        transactions = []

        for row in rows:
            t = Transaction(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
            )
            transactions.append(t)

        cursor.close()

        return transactions

    def update_transaction(self, id: int, transaction: UpdateTransactionDto, type: str):
        cursor = db.cursor()
        cursor.execute(
            "UPDATE transaction SET name = %s, amount = %s WHERE id = %s AND type = %s",
            (transaction.name, transaction.amount, id, type),
        )
        db.commit()
        cursor.close()

    def delete_transaction(self, id: int, type: str):
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM transaction WHERE id = %s AND type = %s", (id, type)
        )
        db.commit()
        cursor.close()
