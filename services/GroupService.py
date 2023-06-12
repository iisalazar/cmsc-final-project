from db import db
from dataclasses import dataclass
from entities.Group import Group
from entities.Person import Person
from typing import List


@dataclass
class CreateGroupDto:
    name: str


class GroupService:
    def view_all_groups(self) -> list:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM grp;")
        rows = cursor.fetchall()

        groups = []

        for row in rows:
            group = {
                "id": row[0],
                "name": row[1],
                "date": row[2],
            }
            groups.append(group)

        return groups

    def create_group(self, dto: CreateGroupDto):
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO grp (name, dateCreated) VALUES (%s, NOW())", (dto.name,)
        )
        db.commit()
        cursor.close()

        return cursor.lastrowid

    def add_person_to_group(self, person_id: int, group_id: int) -> None:
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO person_grp (personId, grpId) VALUES (%s, %s)",
            (person_id, group_id),
        )
        db.commit()
        cursor.close()

    def remove_person_from_group(self, person_id: int, group_id: int) -> None:
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM person_grp WHERE personId = %s AND grpId = %s",
            (person_id, group_id),
        )
        db.commit()
        cursor.close()

    def view_group(self, group_id: int) -> Group | None:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM grp WHERE id = %s", (group_id,))
        row = cursor.fetchone()

        if row is None:
            print("No group found with that id")
            return None

        group = Group(row[0], row[1], row[2])
        return group

    def delete_group(self, group_id: int) -> None:
        cursor = db.cursor()
        # delete transactions first
        cursor.execute("DELETE FROM transaction WHERE grpId = %s", (group_id,))
        # delete person_grp first
        cursor.execute("DELETE FROM person_grp WHERE grpId = %s", (group_id,))
        # delete group
        cursor.execute("DELETE FROM grp WHERE id = %s", (group_id,))
        db.commit()
        cursor.close()

    def update_group(self, group_id: int, dto: CreateGroupDto) -> None:
        cursor = db.cursor()
        cursor.execute("UPDATE grp SET name = %s WHERE id = %s", (dto.name, group_id))
        db.commit()
        cursor.close()

    def remove_all_persons_from_group(self, group_id: int) -> None:
        cursor = db.cursor()
        cursor.execute("DELETE FROM person_grp WHERE grpId = %s", (group_id,))
        db.commit()
        cursor.close()

    def view_all_persons_in_group(self, group_id: int) -> List[Group]:
        cursor = db.cursor()
        cursor.execute(
            "SELECT p.* FROM person AS p INNER JOIN person_grp AS gp ON p.id = gp.personId WHERE gp.grpId = %s",
            (group_id,),
        )

        rows = cursor.fetchall()

        persons: List[Person] = []
        for row in rows:
            persons.append(Person(row[0], row[1], row[2]))

        return persons

    def search_group(self, name: str) -> List[Group]:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM grp WHERE name LIKE %s", ("%" + name + "%",))
        rows = cursor.fetchall()

        groups: List[Group] = []

        for row in rows:
            group = Group(row[0], row[1], row[2])
            groups.append(group)

        return groups

    def view_all_groups_of_person(self, person_id: int) -> List[Group]:
        cursor = db.cursor()
        cursor.execute(
            "SELECT g.* FROM grp AS g INNER JOIN person_grp AS gp ON g.id = gp.grpId WHERE gp.personId = %s",
            (person_id,),
        )

        rows = cursor.fetchall()

        groups: List[Group] = []
        for row in rows:
            groups.append(Group(row[0], row[1], row[2]))

        return groups

    def check_if_person_in_group(self, person_id: int, group_id: int) -> bool:
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM person_grp WHERE personId = %s AND grpId = %s",
            (person_id, group_id),
        )

        row = cursor.fetchone()

        if row is None:
            return False
        return True
