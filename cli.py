from controllers.ReportController import ReportController


class Application:
    def __init__(self) -> None:
        # TODO: Register controllers
        self.register_controllers()

    def register_controllers(self):
        self.controllers = {
            "report": ReportController(),
        }

    def handle_request(self, choice):
        if choice == 4:
            self.controllers["report"].handle_user_input()
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
        """
        )


if __name__ == "__main__":
    app = Application()
    app.run()
