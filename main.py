from db import db
from services.FriendService import FriendService
from services.TransactionService import TransactionService


def run():
    # conect to db
    # execute query

    print("App is running")
    print("Friends:")
    friendService = FriendService()
    friends = friendService.get_friends()
    for friend in friends:
        print(friend)

    transaction = TransactionService()
    transactions = transaction.get_user_transactions(1)
    print("Transactions:")
    for transaction in transactions:
        print(transaction)


if __name__ == "__main__":
    run()
