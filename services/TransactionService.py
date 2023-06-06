from db import db
from entities.Transaction import Transaction


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

        return transactions
