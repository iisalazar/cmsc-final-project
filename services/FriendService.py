from db import db
from entities.Person import Person


class FriendService:
    def get_friends(self):
        cursor = db.cursor()
        cursor.execute("SELECT * FROM person WHERE person.isUser = 0")
        rows = cursor.fetchall()

        friends = []

        for row in rows:
            f = Person(row[0], row[1], False)
            friends.append(f)

        return friends
