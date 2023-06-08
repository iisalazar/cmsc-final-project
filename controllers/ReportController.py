from services.BalanceService import BalanceService
from services.ExpenseService import ExpenseService


class ReportController:
    def __init__(self):
        self.balance_service = BalanceService()
        self.expense_service = ExpenseService()
        self.register_request_method_map()

    def register_request_method_map(self):
        self.request_method_map = {
            1: self.view_all_expenses_within_a_month,
            2: self.view_all_expenses_with_a_friend,
            3: self.view_all_expenses_with_a_group,
            4: self.view_current_balance_from_all_expenses,
            5: self.view_all_friends_with_outstanding_balance,
            6: self.view_all_groups,
            7: self.view_all_groups_with_outstanding_balance,
        }

    def handle_user_input(self):
        # at this point, the user picked option 4
        valid_choices = [
            0,
            1,
            2,
            3,
            4,
            5,
            6,
            7,
        ]
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
0. Exit
1. View all expenses made within a month
2. View all expenses made with a friend
3. View all expenses made with a group
4. View current balance from all expenses
5. View all friends with outstanding balance
6. View all groups
7. View all groups with an outstanding balance
            """
        )

    def view_all_expenses_within_a_month(self):
        result = self.expense_service.get_expenses_for_this_month()
        print("Expenses for this month:")
        for expense in result:
            print(expense)

    def view_all_expenses_with_a_friend(self):
        pass

    def view_all_expenses_with_a_group(self):
        pass

    def view_current_balance_from_all_expenses(self):
        pass

    def view_all_friends_with_outstanding_balance(self):
        pass

    def view_all_groups(self):
        pass

    def view_all_groups_with_outstanding_balance(self):
        pass
