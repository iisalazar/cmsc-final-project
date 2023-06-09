from services.PaymentService import (
    PaymentService,
    CreateFriendPaymentDto,
    CreateGroupPaymentDto,
)
from services.TransactionService import UpdateTransactionDto
from utils.clearScreen import clear_screen


class PaymentController:
    def __init__(self) -> None:
        self.payment_service = PaymentService()
        self.request_method_map = {
            1: self.create_payment,
            2: self.creaate_group_payment,
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
1. Create payment for a person
2. Create payment for a group
3. Update payment
4. Delete payment
5. View all payments
6. Clear screen
"""
        )

    def create_payment(self):
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")
        person_id = int(input("Enter person id: "))

        dto = CreateFriendPaymentDto(
            amount=amount,
            name=name,
            person_id=person_id,
            lender_id=person_id,
            lendee_id=1,
        )
        self.payment_service.create_friend_payment(dto)

    def creaate_group_payment(self):
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")
        group_id = int(input("Enter group id: "))
        lender_id = int(input("Enter lender id: "))
        lendee_id = int(input("Enter lendee id: "))

        dto = CreateGroupPaymentDto(
            amount=amount,
            name=name,
            grp_id=group_id,
            lender_id=lender_id,
            lendee_id=lendee_id,
        )
        self.payment_service.create_group_payment(dto)

    def update_payment(self):
        payment_id = int(input("Enter payment id: "))
        amount = float(input("Enter amount: "))
        name = input("Enter description: ")

        dto = UpdateTransactionDto(
            amount=amount,
            name=name,
        )
        self.payment_service.update_payment(payment_id, dto)

    def delete_payment(self):
        payment_id = int(input("Enter payment id: "))
        self.payment_service.delete_payment(payment_id)

    def view_all_payments(self):
        person_id = int(input("Enter person id: "))
        result = self.payment_service.view_payments(person_id)
        print("Payments:")
        for payment in result:
            print(payment)
