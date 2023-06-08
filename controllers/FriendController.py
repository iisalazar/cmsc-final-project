from services.FriendService import (
    FriendService,
)
from utils.clearScreen import clear_screen


class FriendController:
    def __init__(self) -> None:
        self.friend_servise = FriendService()
        self.request_method_map = {
            1: self.create_friend,
            2: self.update_friend,
            3: self.delete_friend,
            4: self.view_friends,
            5: clear_screen,
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
1. Create a friend
2. Update friend's info
3. Delete a friend
4. View all friends
5. Clear screen
"""
        )

    def create_friend(self):
        name = input("Enter a name: ")

        result = FriendService.add_friend(self, name)

        print(result)

    def update_friend(self):
        id = input("Enter friend Id: ")
        name = input("Enter a new name: ")

        result = FriendService.edit_friend(self, name, id)

        print(result)

    def delete_friend(self):
        id = input("Enter friend Id: ")

        result = FriendService.delete_friend(self, id)

        print(result)

    def view_friends(self):
        result = FriendService.get_friends(self)
        for person in result:
            print(person)
