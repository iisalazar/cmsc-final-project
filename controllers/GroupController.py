from services.GroupService import GroupService, CreateGroupDto
from entities.Group import Group
from utils.clearScreen import clear_screen


class GroupController:
    def __init__(self) -> None:
        self.group_service = GroupService()
        self.request_method_map = {
            1: self.create_group,
            2: self.update_group,
            3: self.delete_group,
            4: self.view_all_groups,
            5: self.add_person_to_group,
            6: self.remove_person_from_group,
            7: self.view_group,
            8: self.view_all_members,
            9: self.remove_members,
            10: self.search_group,
            11: self.view_persons_groups,
            12: clear_screen,
        }

    def handle_user_input(self):
        valid_choices = list(self.request_method_map.keys())

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
1. Create group
2. Update group
3. Delete group
4. View all groups
5. Add person to group
6. Remove person from group
7. View group
8. View all members
9. Remove members
10. Search group
11. View person's groups
12. Clear screen
"""
        )

    def create_group(self):
        name = input("Enter group name: ")
        group = CreateGroupDto(name=name)
        self.group_service.create_group(group)

    def update_group(self):
        _id = int(input("Enter group id: "))
        name = input("Enter group name: ")
        group = CreateGroupDto(name=name)
        self.group_service.update_group(_id, group)

    def delete_group(self):
        _id = int(input("Enter group id: "))
        self.group_service.delete_group(_id)

    def view_all_groups(self):
        groups = self.group_service.view_all_groups()
        for group in groups:
            print(group)

    def add_person_to_group(self):
        group_id = int(input("Enter group id: "))
        person_id = int(input("Enter person id: "))
        self.group_service.add_person_to_group(person_id, group_id)

    def remove_person_from_group(self):
        group_id = int(input("Enter group id: "))
        person_id = int(input("Enter person id: "))
        self.group_service.remove_person_from_group(person_id, group_id)

    def view_group(self):
        _id = int(input("Enter group id: "))
        group = self.group_service.view_group(_id)
        print("\nGroup ID: " + str(group.id))
        print("Name: " + group.name)
        print("Date Created: " + str(group.dateCreated))
        print("------------------------------------")

    def view_all_members(self):
        _id = int(input("Enter group id: "))
        print("\nMembers in Group with ID: " + str(_id) + "\n")
        members = self.group_service.view_all_persons_in_group(_id)
        for member in members:
            print("Person ID: " + str(member.id))
            print("Name: " + member.name)
            print("------------------------------------")

    def remove_members(self):
        print("\nChoose Group ID to delete all members:\n")

        choices = self.group_service.view_all_groups()
        for group in choices:
            print("[" + str(group["id"]) + "]\t" + group["name"])

        _id = input("\nEnter group id: ")
        counter = 0

        for group in choices:
            counter += 1
            if str(group["id"]) == str(_id):
                self.group_service.remove_all_persons_from_group(int(_id))
                print("Successfully removed all members from " + group["name"])
                break
            elif counter == len(choices):
                print("Group ID not found.")

    def search_group(self):
        name = input("Enter group name: ")
        groups = self.group_service.search_group(name)
        print("\nGroups found with name: " + name + "\n")
        for group in groups:
            print("Group ID: " + str(group.id))
            print("Group Name: " + group.name)
            print("------------------------------------")

    def view_persons_groups(self):
        person_id = int(input("Enter person id: "))
        groups = self.group_service.view_all_groups_of_person(person_id)
        print("\nGroups joined by a person with id: " + str(person_id) + "\n")
        for group in groups:
            print("Group ID: " + str(group.id))
            print("Name: " + group.name)
            print("Date Created: " + str(group.dateCreated))
            print("------------------------------------")
