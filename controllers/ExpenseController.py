from services.ExpenseService import ExpenseService
from utils.clearScreen import clear_screen


class ExpenseController:
    def __init__(self) -> None:
        self.expense_service = ExpenseService()
        self.request_method_map = {
            1: self.create_expense,
            2: self.create_expense_group,
            3: self.update_expense,
            4: self.delete_expense,
            5: self.view_all_expenses,
            6: clear_screen,
        }

    def handle_user_input(self):
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
0. Go Back
1. Create expense for a person
2. Create expense for a group
3. Update expense
4. Delete expense
5. View all expenses
6. Clear screen
"""
        )

    def create_expense(self):
        amount = float(input("Enter amount: "))
        name = input("Enter name: ")

    def update_expense(self):
        pass

    def delete_expense(self):
        pass

    def view_all_expenses(self):
        pass
