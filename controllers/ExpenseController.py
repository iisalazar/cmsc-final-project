from services.ExpenseService import ExpenseService
from utils.clearScreen import clear_screen


class ExpenseController:
    def __init__(self) -> None:
        self.expense_service = ExpenseService()
        self.request_method_map = {
            1: self.create_expense,
            2: self.update_expense,
            3: self.delete_expense,
            4: self.view_all_expenses,
            5: clear_screen,
        }

    def handle_user_input(self):
        valid_choices = [0, 1, 2, 3, 4, 5]
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
1. Create expense
2. Update expense
3. Delete expense
4. View all expenses
5. Clear screen
"""
        )

    def create_expense(self):
        pass

    def update_expense(self):
        pass

    def delete_expense(self):
        pass

    def view_all_expenses(self):
        pass
