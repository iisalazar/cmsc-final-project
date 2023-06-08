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
    
    
    def get_friend_by_id(self,  friend_id: int) -> Person:      
        cursor = db.cursor()
        cursor.execute("SELECT * FROM person WHERE person.id = %s", (friend_id,))
        friend = cursor.fetchone()


        f = Person(friend[0], friend[1], friend[2])

        return f
