"""
Implement the ff. methods

1. Search transaction
- by name
- by id
- by person id
- by group id
- by lender
- by lendee
- by date range. 
"""
from services.TransactionService import TransactionService, UpdateTransactionDto
from services.ExpenseService import (
    ExpenseService,
    CreateFriendExpenseDto,
    CreateGroupExpenseDto,
)


def run():
    print("App is running")
    transaction = TransactionService()

    transactions = transaction.search_transactions("1-to-1")
    print("Transactions:")
    for t in transactions:
        print(t)

    expense = ExpenseService()

    expense.create_friend_expense(
        CreateFriendExpenseDto(
            amount=100,
            name="1-to-1",
            date="2021-01-01",
            person_id=1,
            lender_id=1,
            lendee_id=2,
        )
    )

    expense.create_group_expense(
        CreateGroupExpenseDto(
            amount=100, name="1-to-1", date="2021-01-01", grp_id=1, lender_id=1
        )
    )

    # updating an existing transaction
    update_dto = UpdateTransactionDto("1-to-123", 1000)

    expense.update_expense(16, update_dto)

    # deleting an existing transaction
    expense.delete_expense(17)

    transactions = transaction.search_transactions("1-to-1")

    print("Transactions:")
    for t in transactions:
        print(t)


if __name__ == "__main__":
    run()
