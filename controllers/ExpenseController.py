from services.ExpenseService import (
    ExpenseService,
    CreateFriendExpenseDto,
    CreateGroupExpenseDto,
)
from services.BalanceService import BalanceService
from services.TransactionService import UpdateTransactionDto
from utils.clearScreen import clear_screen


class ExpenseController:
    CHOICE_PROMPT = """
----------------🅼 🅴 🅽 🆄----------------
0. Go Back
1. Create expense for a person
2. Create expense for a group
3. Update expense
4. Delete expense
5. View all expenses 
6. Clear screen
---------------------------------------
"""
    AMOUNT_PROMPT = "Enter amount: "
    DESCRIPTION_PROMPT = "Enter description: "
    PERSON_ID_PROMPT = "Enter person id: "
    GROUP_ID_PROMPT = "Enter group id: "
    EXPENSE_ID_PROMPT = "Enter expense id: "
    PERSON_ID_INPUT = "Enter person id: "
    LENDER_ID_INPUT = "Enter lender id: "
    LENDEE_ID_INPUT = "Enter lendee id: "

    def __init__(self):
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
        valid_choices = list(self.request_method_map.keys()) + [0]
        choice = -1
        while choice != 0:
            self.print_choices()
            choice = self.get_valid_integer_input("Enter choice: ", valid_choices)
            if choice == -1:
                print("Invalid choice")
                continue
            elif choice == 0:
                break
            elif choice is None:
                print("Invalid input. Please enter a valid number.")
                continue
            self.request_method_map[choice]()

    def print_choices(self):
        print(self.CHOICE_PROMPT)

    def create_expense(self):
        amount = self.get_valid_float_input(self.AMOUNT_PROMPT)
        name = input(self.DESCRIPTION_PROMPT)
        person_id = self.get_valid_integer_input(self.PERSON_ID_PROMPT)
        lender_id = self.get_valid_integer_input(self.LENDER_ID_INPUT)
        lendee_id = self.get_valid_integer_input(self.LENDEE_ID_INPUT)


        if amount is None or person_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = CreateFriendExpenseDto(
            amount=amount,
            name=name,
            person_id=person_id,
            lender_id=lender_id,
            lendee_id=lendee_id,
        )
        result = self.expense_service.create_friend_expense(dto)

        print("Created expense with id:", result.id)

    def create_group_expense(self):
        amount = self.get_valid_float_input(self.AMOUNT_PROMPT)
        name = input(self.DESCRIPTION_PROMPT)
        group_id = self.get_valid_integer_input(self.GROUP_ID_PROMPT)
        lender_id = self.get_valid_integer_input("Enter lender id: ")

        if amount is None or group_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = CreateGroupExpenseDto(
            amount=amount,
            name=name,
            grp_id=group_id,
            lender_id=lender_id,
        )

        self.expense_service.create_group_expense(dto)

    def update_expense(self):
        expense_id = self.get_valid_integer_input(self.EXPENSE_ID_PROMPT)
        amount = self.get_valid_float_input(self.AMOUNT_PROMPT)
        name = input(self.DESCRIPTION_PROMPT)

        if expense_id is None or amount is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = UpdateTransactionDto(
            amount=amount,
            name=name,
        )

        self.expense_service.update_expense(expense_id, dto)

    def delete_expense(self):
        expense_id = self.get_valid_integer_input(self.EXPENSE_ID_PROMPT)

        if expense_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        self.expense_service.delete_expense(expense_id)

    def view_all_expenses(self):
        person_id = self.get_valid_integer_input(self.PERSON_ID_INPUT)

        if person_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        result = self.expense_service.get_expenses_with_friend(person_id)
        print("Expenses with friend:")
        for expense in result:
            print(expense)

    @staticmethod
    def get_valid_integer_input(prompt, valid_choices=None):
        try:
            value = int(input(prompt))
            if valid_choices is not None and value not in valid_choices:
                return None
            return value
        except ValueError:
            return None

    @staticmethod
    def get_valid_float_input(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            return None
