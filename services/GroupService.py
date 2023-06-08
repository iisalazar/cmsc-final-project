from db import db


class GroupService:
    def view_all_groups(self) -> list:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM grp;")
        rows = cursor.fetchall()

        groups = []
        
        for row in rows:
            group ={
                "id": row[0],
                "name": row[1],
                "date": row[2],
            }
            groups.append(group)

        return groups