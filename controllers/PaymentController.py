from services.FriendService import FriendService
from services.GroupService import GroupService
from services.PaymentService import (
    PaymentService,
    CreateFriendPaymentDto,
    CreateGroupPaymentDto,
)
from services.TransactionService import UpdateTransactionDto
from utils.clearScreen import clear_screen


class PaymentController:
    CHOICE_PROMPT = """
----------------🅼 🅴 🅽 🆄----------------
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
        self.friend_service = FriendService()
        self.group_service = GroupService()
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
            """
,-----------------------------------------------------------,
| █▀█ ▄▀█ █▄█ █▀▄▀█ █▀▀ █▄░█ ▀█▀  █▀ █▀▀ █▀▀ ▀█▀ █ █▀█ █▄░█ |
| █▀▀ █▀█ ░█░ █░▀░█ ██▄ █░▀█ ░█░  ▄█ ██▄ █▄▄ ░█░ █ █▄█ █░▀█ |
'-----------------------------------------------------------' """
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
        payer_id = self.get_valid_integer_input("Enter person ID who wants to pay: ")
        payee_id = self.get_valid_integer_input(
            "Enter person ID who will receive the payment: "
        )

        if amount is None or payer_id is None or payee_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        # check if person exists
        payer = self.friend_service.get_friend_by_id(payer_id)
        payee = self.friend_service.get_friend_by_id(payee_id)

        if payer is None:
            print("Payer does not exist")
            return

        if payee is None:
            print("Payee does not exist")
            return

        dto = CreateFriendPaymentDto(
            amount=amount,
            name=name,
            person_id=payee_id,
            lender_id=payer_id,
            lendee_id=payee_id,
        )
        transaction = self.payment_service.create_friend_payment(dto)

        print("Created new payment")
        print("Payment ID: ", transaction.id)
        print("Amount: ", transaction.amount)
        print("Description: ", transaction.name)
        print("Payer ID: ", transaction.lenderId)
        print("Payee ID: ", transaction.lendeeId)
        print("======================")

    def create_group_payment(self):
        amount = self.get_valid_float_input("Enter amount: ")
        name = input("Enter description: ")
        group_id = self.get_valid_integer_input("Enter group id: ")
        payer_id = self.get_valid_integer_input("Enter payer's ID: ")
        payee_id = self.get_valid_integer_input("Enter payee's ID: ")

        if amount is None or group_id is None or payer_id is None or payee_id is None:
            print("Invalid input. Please enter a valid number.")
            return

        group = self.group_service.view_group(group_id)
        payer = self.friend_service.get_friend_by_id(payer_id)
        payee = self.friend_service.get_friend_by_id(payee_id)

        if group is None:
            print("Group does not exist")
            return

        if payer is None:
            print("Payer does not exist")
            return

        if payee is None:
            print("Payee does not exist")
            return

        # check if both payer and payee are in the group
        person_in_group = self.group_service.check_if_person_in_group(
            payer_id, group_id
        )
        if not person_in_group:
            print("Payer is not in the group")
            return

        person_in_group = self.group_service.check_if_person_in_group(
            payee_id, group_id
        )
        if not person_in_group:
            print("Payee is not in the group")
            return

        dto = CreateGroupPaymentDto(
            amount=amount,
            name=name,
            grp_id=group_id,
            lender_id=payer_id,
            lendee_id=payee_id,
        )
        transaction = self.payment_service.create_group_payment(dto)
        print("\nCreated new payment")
        print("\tPayment ID: ", transaction.id)
        print("\tAmount: ", transaction.amount)
        print("\tDescription: ", transaction.name)
        print("\tPayer ID: ", transaction.lenderId)
        print("\tPayee ID: ", transaction.lendeeId)
        print("\tGroup ID: ", transaction.grpId)
        print("======================")

    def update_payment(self):
        payment_id = self.get_valid_integer_input("Enter payment id: ")
        amount = self.get_valid_float_input("Enter amount: ")
        name = input("Enter description: ")

        if payment_id is None or amount is None:
            print("Invalid input. Please enter a valid number.")
            return

        payment = self.payment_service.get_payment(payment_id)

        if payment is None:
            print("Payment does not exist")
            return

        dto = UpdateTransactionDto(
            amount=amount,
            name=name,
        )
        self.payment_service.update_payment(payment_id, dto)

        print("\nUpdated payment")
        print("\tPayment ID: ", payment_id)
        print("\tAmount: ", amount)
        print("\tDescription: ", name)
        print("======================")

    def delete_payment(self):
        payment_id = self.get_valid_integer_input("Enter payment id: ")

        if payment_id is None:
            print("Invalid input. Please enter a valid number.")
            return
        payment = self.payment_service.get_payment(payment_id)

        if payment is None:
            print("Payment does not exist")
            return
        self.payment_service.delete_payment(payment_id)

        print("\nDeleted payment with id ", payment_id)

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
