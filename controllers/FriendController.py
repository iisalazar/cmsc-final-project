from services.FriendService import (
    FriendService,
)
from utils.clearScreen import clear_screen


class FriendController:
    def __init__(self) -> None:
        self.friend_service = FriendService()
        self.request_method_map = {
            1: self.create_friend,
            2: self.update_friend,
            3: self.delete_friend,
            4: self.view_friends,
            5: clear_screen,
        }

    def handle_user_input(self):
        valid_choices = ["0", "1", "2", "3", "4", "5", "6"]
        choice = -1
        while choice != 0:
            self.print_choices()
            choice = input("Enter choice: ")
            if choice not in valid_choices or not choice.isnumeric():
                print("Invalid choice")
                continue
            if choice == "0":
                break
            self.request_method_map[int(choice)]()

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

        result = self.friend_service.add_friend(name)

        print(result)

    def update_friend(self):
        print("\nChoose Person ID to edit\n")

        choices = self.friend_service.get_friends()
        for person in choices:
            print("[" + str(person.id) + "]\t" + person.name)

        id = input("\nEnter friend ID: ")
        counter = 0

        for person in choices:
            counter += 1
            if str(person.id) == id:
                name = input("Enter a new name: ")
                result = self.friend_service.edit_friend(name, id)
                print(result)
                break
            elif counter == len(choices):
                print("Friend ID not found.")

    def delete_friend(self):
        print("\nChoose Person ID to delete\n")

        choices = self.friend_service.get_friends()
        for person in choices:
            print("[" + str(person.id) + "]\t" + person.name)

        id = input("\nEnter friend Id: ")
        counter = 0

        for person in choices:
            counter += 1
            if str(person.id) == id:
                result = self.friend_service.delete_friend(id)
                print(result)
                break
            elif counter == len(choices):
                print("Friend ID not found.")

    def view_friends(self):
        result = self.friend_service.get_friends()
        print("\nAll Friends:\n")
        for person in result:
            print("Person ID: " + str(person.id))
            print("Name: " + person.name)
            print("------------------------------")
