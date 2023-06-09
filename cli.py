from controllers.ReportController import ReportController
from controllers.ExpenseController import ExpenseController
from controllers.PaymentController import PaymentController
from controllers.FriendController import FriendController
from controllers.GroupController import GroupController
from utils.clearScreen import clear_screen


class Application:
    def __init__(self) -> None:
        self.register_controllers()

    def register_controllers(self):
        self.controllers = {
            "report": ReportController(),
            "expense": ExpenseController(),
            "payment": PaymentController(),
            "friend": FriendController(),
            "group": GroupController(),
        }

    def handle_request(self, choice):
        if choice == 0:
            print(
    '''
,--------------------------------,
| █▄▄ █▄█ █▀▀  █▄▄ █▄█ █▀▀ ░ ░ ░ |
| █▄█ ░█░ ██▄  █▄█ ░█░ ██▄ ▄ ▄ ▄ |
'--------------------------------' '''
        )
            return
        if choice == 1:
            self.controllers["expense"].handle_user_input()
        elif choice == 2:
            self.controllers["payment"].handle_user_input()
        elif choice == 3:
            self.controllers["friend"].handle_user_input()
        if choice == 4:
            self.controllers["group"].handle_user_input()
        elif choice == 5:
            self.controllers["report"].handle_user_input()
        elif choice == 6:
            clear_screen()
        else:
            print("Invalid choice")

    def run(self) -> None:
        choice = -1
        print(
    '''
,-------------------------------------------------------,
| █▀ █▀█ █░░ █ ▀█▀ █░█░█ █ █▀ █▀▀  █▀▀ █░░ █▀█ █▄░█ █▀▀ |
| ▄█ █▀▀ █▄▄ █ ░█░ ▀▄▀▄▀ █ ▄█ ██▄  █▄▄ █▄▄ █▄█ █░▀█ ██▄ |
'-------------------------------------------------------' '''
        )
        while choice != 0:
            self.print_choices()
            choice = int(input("Enter choice: "))
            self.handle_request(choice)

    def print_choices(self):
        print(
            """

---------🅼 🅴 🅽 🆄------------
0. Exit
1. CRUD expense
2. CRUD payment
3. CRUD friend
4. CRUD group
5. Generate report
6. Clear screen
-------------------------------
        """
        )


if __name__ == "__main__":
    app = Application()
    app.run()
