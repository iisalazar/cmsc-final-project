from services.ExpenseService import (
    ExpenseService,
    CreateFriendExpenseDto,
    CreateGroupExpenseDto,
)
from services.BalanceService import BalanceService
from services.TransactionService import UpdateTransactionDto
from utils.clearScreen import clear_screen


class ExpenseController:
    def __init__(self) -> None:
        self.expense_service = ExpenseService()
        self.balance_service = BalanceService()
        self.request_method_map = {
            1: self.create_expense,
            2: self.create_group_expense,
            3: self.update_expense,
            4: self.delete_expense,
            5: self.view_all_expenses,
            6: clear_screen,
        }

    def handle_user_input(self):
        print(
    '''
,-----------------------------------------------------------,
| █▀▀ ▀▄▀ █▀█ █▀▀ █▄░█ █▀ █▀▀ █▀  █▀ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ |
| ██▄ █░█ █▀▀ ██▄ █░▀█ ▄█ ██▄ ▄█  ▄█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ |
'-----------------------------------------------------------' '''
        )
        valid_choices = [0, 1, 2, 3, 4, 5, 6]
        choice = -1
        while choice != 0:
            self.print_choices()
            choice = int(input("Enter choice: "))
            if choice not in valid_choices:
                print("Invalid choice")
                continue
            if choice == 0:
                break
            self.request_method_map[choice]()

    def print_choices(self):
        print(
            """
---------🅼 🅴 🅽 🆄--------------
0. Go Back
1. Create expense for a person
2. Create expense for a group
3. Update expense
4. Delete expense
5. View all expenses 
6. Clear screen
--------------------------------
"""
        )

    def create_expense(self):
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")
        person_id = int(input("Enter person id: "))

        dto = CreateFriendExpenseDto(
            amount=amount,
            name=name,
            person_id=person_id,
            lender_id=1,
            lendee_id=person_id,
        )
        result = self.expense_service.create_friend_expense(dto)

        print("Created expense with id: ", result.id)

    def create_group_expense(self):
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")
        group_id = int(input("Enter group id: "))

        dto = CreateGroupExpenseDto(
            amount=amount,
            name=name,
            grp_id=group_id,
            lender_id=1,
        )

        self.expense_service.create_group_expense(dto)

    def update_expense(self):
        _id = int(input("Enter expense id: "))
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")

        dto = UpdateTransactionDto(
            amount=amount,
            name=name,
        )

        self.expense_service.update_expense(_id, dto)

    def delete_expense(self):
        _id = int(input("Enter expense id: "))
        self.expense_service.delete_expense(_id)

    def view_all_expenses(self):
        person_id = int(input("Enter person id: "))
        result = self.expense_service.get_expenses_with_friend(person_id)
        print("Expenses with friend:")
        for expense in result:
            print(expense)
