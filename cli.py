from controllers.ReportController import ReportController
from controllers.ExpenseController import ExpenseController
from utils.clearScreen import clear_screen


class Application:
    def __init__(self) -> None:
        self.register_controllers()

    def register_controllers(self):
        self.controllers = {
            "report": ReportController(),
            "expense": ExpenseController(),
        }

    def handle_request(self, choice):
        if choice == 0:
            print("Good bye!")
            return
        if choice == 1:
            self.controllers["expense"].handle_user_input()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        if choice == 4:
            self.controllers["report"].handle_user_input()
        elif choice == 5:
            clear_screen()
        else:
            print("Invalid choice")

    def run(self) -> None:
        choice = -1

        while choice != 0:
            self.print_choices()
            choice = int(input("Enter choice: "))
            self.handle_request(choice)

    def print_choices(self):
        print(
            """
0. Exit
1. CRUD expense
2. CRUD friend
3. CRUD group
4. Generate report
5. Clear screen
        """
        )


if __name__ == "__main__":
    app = Application()
    app.run()
