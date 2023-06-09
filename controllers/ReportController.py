from services.FriendService import FriendService
from services.BalanceService import BalanceService
from services.ExpenseService import ExpenseService
from services.GroupService import GroupService
from utils.clearScreen import clear_screen


class ReportController:
    CHOICE_PROMPT = """
-------------------🅼 🅴 🅽 🆄-----------------------
0. Go Back
1. View all expenses made within a month
2. View all expenses made with a friend
3. View all expenses made with a group
4. View current balance from all expenses
5. View all friends with outstanding balance
6. View all groups
7. View all groups with an outstanding balance
8. Clear screen
-------------------------------------------------
"""

    def __init__(self):
        self.balance_service = BalanceService()
        self.expense_service = ExpenseService()
        self.friend_service = FriendService()
        self.group_service = GroupService()
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
            8: clear_screen,
        }

    def handle_user_input(self):
        print(
            """
,-------------------------------------------------------,
| █▀█ █▀▀ █▀█ █▀█ █▀█ ▀█▀ █▀  █▀ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ |
| █▀▄ ██▄ █▀▀ █▄█ █▀▄ ░█░ ▄█  ▄█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ |
'-------------------------------------------------------' """
        )
        # at this point, the user picked option 4
        valid_choices = list(self.request_method_map.keys()) + [0]
        choice = -1
        while choice != 0:
            self.print_choices()
            choice = self.get_valid_integer_input("Enter choice: ", valid_choices)
            if choice == -1:
                print("Invalid choice")
                continue
            if choice == 0:
                break
            self.request_method_map[choice]()

    def print_choices(self):
        print(self.CHOICE_PROMPT)

    def view_all_expenses_within_a_month(self):
        result = self.expense_service.get_expenses_for_this_month()

        if len(result) == 0:
            print("You have no expenses within this month")
        else:
            print("Expenses for this month: \n")
            for expense in result:
                lender = self.friend_service.get_friend_by_id(expense.lenderId)
                lendee = self.friend_service.get_friend_by_id(expense.lendeeId)
                print("Transation id: " + str(expense.id))
                print("Name: " + expense.name)
                print("Amount: " + str(expense.amount))
                print("Date: " + str(expense.dateCreated))
                print("Lender: " + lender.name)
                print("Lendee: " + lendee.name)
                print("Type: " + expense.type)
                print("------------------------------------")

    def view_all_expenses_with_a_friend(self):
        friend_id = self.get_valid_integer_input("Enter friend id: ")

        if friend_id is None:
            print("Invalid friend id")
            return

        result = self.expense_service.get_expenses_with_friend(friend_id)
        friend = self.friend_service.get_friend_by_id(friend_id)

        if len(result) == 0:
            print("You have no expenses with " + friend.name)
        else:
            print("\nYour expenses with " + friend.name + ":\n")
            for expense in result:
                lender = self.friend_service.get_friend_by_id(expense.lenderId)
                lendee = self.friend_service.get_friend_by_id(expense.lendeeId)

                print("Transation id: " + str(expense.id))
                print("Name: " + expense.name)
                print("Amount: " + str(expense.amount))
                print("Date: " + str(expense.dateCreated))
                print("Lender: " + lender.name)
                print("Lendee: " + lendee.name)
                print("Type: " + expense.type)
                print("------------------------------------")

    def view_all_expenses_with_a_group(self):
        group_id = self.get_valid_integer_input("Enter group id: ")

        if group_id is None:
            print("Invalid group id")
            return

        result = self.expense_service.get_group_expenses(group_id)

        if len(result) == 0:
            print("You have no expenses with this group")
        else:
            print("\nExpenses with group:\n")
            for expense in result:
                lender = self.friend_service.get_friend_by_id(expense.lenderId)
                lendee = self.friend_service.get_friend_by_id(expense.lendeeId)

                print("Transaction id: " + str(expense.id))
                print("Transaction name: " + expense.name)
                print("Amount: " + str(expense.amount))
                print("Date: " + str(expense.dateCreated))
                print("Lender: " + lender.name)
                print("Lendee: " + lendee.name)
                print("Type: " + expense.type)
                print("------------------------------------")

    def view_current_balance_from_all_expenses(self):
        result = self.balance_service.get_current_balance()
        print("Current balance: ", result)

    def view_all_friends_with_outstanding_balance(self):
        result = self.balance_service.get_friends_with_balance()

        if len(result) == 0:
            print("All friends have no outstanding balance")
        else:
            print("\nFriends with outstanding balance:\n")
            for friend_id, balance in result:
                friend = self.friend_service.get_friend_by_id(friend_id)
                print("Friend: " + friend.name)
                print("Amount: " + str(balance))
                print("------------------------------------")

    def view_all_groups(self):
        result = self.group_service.view_all_groups()

        if len(result) == 0:
            print("There are no existing groups")
        else:
            print("\nAll groups: \n")
            for group in result:
                print("Group ID: " + str(group["id"]))
                print("Name: " + group["name"])
                print("Date created: " + str(group["date"]))
                print("------------------------------------")

    def view_all_groups_with_outstanding_balance(self):
        result = self.balance_service.get_groups_with_outstanding_balance()

        if len(result) == 0:
            print("All groups have no outstanding balance")
        else:
            print("\nGroups with outstanding balance:\n")
            for group_id, balance in result:
                print("Group id: " + str(group_id))
                print("Amount: " + str(balance))
                print("------------------------------------")

    @staticmethod
    def get_valid_integer_input(prompt, valid_choices=None):
        try:
            value = int(input(prompt))
            if valid_choices is not None and value not in valid_choices:
                return None
            return value
        except ValueError:
            return None
