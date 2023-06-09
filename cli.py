from controllers.ReportController import ReportController
from controllers.ExpenseController import ExpenseController
from controllers.PaymentController import PaymentController
from controllers.FriendController import FriendController
from controllers.GroupController import GroupController
from utils.clearScreen import clear_screen

from db import db
from services.FriendService import (
    FriendService,
)
from entities.Person import Person



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
        while True:
            has_user = self.get_user()

            if has_user:
                while choice != 0:
                    self.print_choices()
                    choice = int(input("Enter choice: "))
                    self.handle_request(choice)
                break
            else:
                print(
    '''
,-----------------------------------,
| █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀ █ |
| ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄ ▄ |
'-----------------------------------' '''
        )
                user = input("Enter your name to start: ")
                self.add_user(user)

    def get_user(self):
        cursor = db.cursor()
        cursor.execute(
            "SELECT * from person where isUser = 1"
        )
        user = cursor.fetchone()

        if not user:
            return False
        else:
            u = Person(user[0], user[1], user[2])

            return True
    
    def add_user(self, name):
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO person (name, isUser) VALUES (%s, true)", (name,)
        )
        db.commit()
        cursor.close()

    def print_choices(self):
        print(
    '''
,-------------------------------------------------------,
| █▀ █▀█ █░░ █ ▀█▀ █░█░█ █ █▀ █▀▀  █▀▀ █░░ █▀█ █▄░█ █▀▀ |
| ▄█ █▀▀ █▄▄ █ ░█░ ▀▄▀▄▀ █ ▄█ ██▄  █▄▄ █▄▄ █▄█ █░▀█ ██▄ |
'-------------------------------------------------------' '''
        )
        print(
            """

------------🅼 🅴 🅽 🆄------------
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
