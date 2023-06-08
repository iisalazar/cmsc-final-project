from db import db
from dataclasses import dataclass
from entities.Person import Person
from typing import List
from entities.Transaction import Transaction
from services.TransactionService import TransactionService, UpdateTransactionDto


@dataclass
class CreateExpenseDto:
    amount: int
    name: str


@dataclass
class CreateFriendExpenseDto(CreateExpenseDto):
    person_id: int
    lender_id: int
    lendee_id: int


@dataclass
class CreateGroupExpenseDto(CreateExpenseDto):
    grp_id: int
    lender_id: int


@dataclass
class UpdateExpenseDto:
    amount: int
    name: str


class ExpenseService(TransactionService):
    def __init__(self):
        super().__init__()

    def create_friend_expense(self, expense: CreateFriendExpenseDto) -> Transaction:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO transaction (name, amount, personId, grpId, lenderId, lendeeId, type, dateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())",
            (
                expense.name,
                expense.amount,
                expense.person_id,
                None,
                expense.lender_id,
                expense.lendee_id,
                "expense",
            ),
        )
        db.commit()

        cursor.close()
        return Transaction(
            cursor.lastrowid,
            expense.name,
            expense.amount,
            None,
            expense.person_id,
            None,
            expense.lender_id,
            expense.lendee_id,
            "expense",
        )

    def create_group_expense(self, expense: CreateGroupExpenseDto) -> None:
        cursor = db.cursor()

        # creating a group expense creates invididual expenses for each member of the group
        cursor.execute(
            "SELECT p.* FROM person AS p INNER JOIN person_grp AS gp ON p.id = gp.personId WHERE gp.grpId = %s",
            (expense.grp_id,),
        )

        rows = cursor.fetchall()

        persons: List[Person] = []
        for row in rows:
            persons.append(Person(row[0], row[1], row[2]))

        print(persons)

        # creating a group expense creates invididual expenses for each member of the group
        for person in persons:
            cursor.execute(
                "INSERT INTO transaction (name, amount, personId, grpId, lenderId, lendeeId, type, dateCreated) VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())",
                (
                    expense.name,
                    expense.amount / len(persons),
                    None,
                    expense.grp_id,
                    expense.lender_id,
                    person.id,
                    "expense",
                ),
            )
        db.commit()
        cursor.close()

    def update_expense(self, id: int, expense: UpdateTransactionDto):
        self.update_transaction(id, expense, type="expense")

    def delete_expense(self, id: int):
        self.delete_transaction(id, "expense")

    def get_expenses_for_this_month(self) -> List[Transaction]:
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM transaction AS t WHERE t.type = 'expense' AND t.dateCreated BETWEEN DATE_FORMAT(NOW(), '%Y-%m-01') AND LAST_DAY(NOW())"
        )
        rows = cursor.fetchall()
        result: List[Transaction] = []
        cursor.close()

        for row in rows:
            result.append(Transaction(*row))

        return result

    def get_expenses_with_friend(self, friend_id: int) -> List[Transaction]:
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM transaction AS t WHERE t.type = 'expense' AND personId=%s",
            (friend_id,),
        )

        rows = cursor.fetchall()

        result: List[Transaction] = []

        cursor.close()

        for row in rows:
            result.append(Transaction(*row))

        return result

    def get_group_expenses(self, group_id: int) -> List[Transaction]:
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM transaction AS t WHERE t.type = 'expense' AND grpId=%s",
            (group_id,),
        )

        rows = cursor.fetchall()

        result: List[Transaction] = []

        cursor.close()

        for row in rows:
            result.append(Transaction(*row))

        return result
