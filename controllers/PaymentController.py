from services.PaymentService import (
    PaymentService,
    CreateFriendPaymentDto,
    CreateGroupPaymentDto,
)
from services.TransactionService import UpdateTransactionDto
from utils.clearScreen import clear_screen


class PaymentController:
    CHOICE_PROMPT = """
---------------🅼 🅴 🅽 🆄---------------
0. Go Back
1. Create payment for a person
2. Create payment for a group
3. Update payment
4. Delete payment
5. View all payments
6. Clear screen
---------------------------------------
"""

    def __init__(self):
        self.payment_service = PaymentService()
        self.request_method_map = {
            1: self.create_payment,
            2: self.create_group_payment,
            3: self.update_payment,
            4: self.delete_payment,
            5: self.view_all_payments,
            6: clear_screen,
        }

    def handle_user_input(self):
        print(
    '''
,-----------------------------------------------------------,
| █▀█ ▄▀█ █▄█ █▀▄▀█ █▀▀ █▄░█ ▀█▀  █▀ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ |
| █▀▀ █▀█ ░█░ █░▀░█ ██▄ █░▀█ ░█░  ▄█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ |
'-----------------------------------------------------------' '''
        )
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

    def create_payment(self):
        amount = self.get_valid_float_input("Enter amount: ")
        name = input("Enter description: ")
        person_id = self.get_valid_integer_input("Enter person id: ")

        if amount is None or person_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = CreateFriendPaymentDto(
            amount=amount,
            name=name,
            person_id=person_id,
            lender_id=person_id,
            lendee_id=1,
        )
        self.payment_service.create_friend_payment(dto)

    def create_group_payment(self):
        amount = self.get_valid_float_input("Enter amount: ")
        name = input("Enter description: ")
        group_id = self.get_valid_integer_input("Enter group id: ")
        lender_id = self.get_valid_integer_input("Enter lender id: ")
        lendee_id = self.get_valid_integer_input("Enter lendee id: ")

        if amount is None or group_id is None or lender_id is None or lendee_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = CreateGroupPaymentDto(
            amount=amount,
            name=name,
            grp_id=group_id,
            lender_id=lender_id,
            lendee_id=lendee_id,
        )
        self.payment_service.create_group_payment(dto)

    def update_payment(self):
        payment_id = self.get_valid_integer_input("Enter payment id: ")
        amount = self.get_valid_float_input("Enter amount: ")
        name = input("Enter description: ")

        if payment_id is None or amount is None:
            print("Invalid input. Please enter a valid number.")
            return

        dto = UpdateTransactionDto(
            amount=amount,
            name=name,
        )
        self.payment_service.update_payment(payment_id, dto)

    def delete_payment(self):
        payment_id = self.get_valid_integer_input("Enter payment id: ")

        if payment_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        self.payment_service.delete_payment(payment_id)

    def view_all_payments(self):
        person_id = self.get_valid_integer_input("Enter person id: ")

        if person_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        result = self.payment_service.view_payments(person_id)
        print("Payments:")
        for payment in result:
            print(payment)

    @staticmethod
    def get_valid_integer_input(prompt, valid_choices=None):
        try:
            value = int(input(prompt))
            if valid_choices is not None and value not in valid_choices:
                return None
            return value
        except ValueError:
            return None

    @staticmethod
    def get_valid_float_input(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            return None
