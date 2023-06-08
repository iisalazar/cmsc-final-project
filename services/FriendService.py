from db import db
from entities.Person import Person


class FriendService:
    def add_friend(self, name):
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO person (name, isUser) VALUES (%s, false)", (name,)
        )
        db.commit()
        cursor.close()
        return f"Successfully added a friend named {name}"
    
    def get_friends(self):
        db.reconnect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM person WHERE person.isUser = 0")
        rows = list(cursor.fetchall())

        friends = []

        for row in rows:
            # f = str(list(row)[0])
            f = Person(row[0],  row[1], row[2])
            friends.append(f)
        
        cursor.close()
        return friends
    
    def delete_friend(self, id):
        db.reconnect()
        cursor = db.cursor()
        cursor.execute(
            'DELETE FROM transaction WHERE lenderId = %s OR lendeeId = %s', (id, id,)
        )
        cursor.execute(
            'DELETE FROM person_grp WHERE personId = %s', (id,)
        )
        cursor.execute(
            'DELETE FROM person WHERE id = %s', (id,)
        )
        db.commit()
        cursor.close()
        
        return f"Successfully deleted a friend with id: {id}"
    
    def edit_friend(self, name, id):
        # db.reconnect()
        cursor = db.cursor()
        cursor.execute(
            "UPDATE person SET name=%s where id=%s", (name, id)
        )

        db.commit()
        cursor.close()
        
        return f"Successfully edited a friend with id: {id}"
