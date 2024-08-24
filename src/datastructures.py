
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"last_name": last_name,
             "id": self._generateId(),
             "first_name": "John",
             "age": "33",
             "lucky_numbers":[7,13,22]
            },
               {"last_name": last_name,
             "id": self._generateId(),
             "first_name": "Jane",
             "age": "35",
             "lucky_numbers":[10,14,3]
            },
               {"last_name": last_name,
             "id": self._generateId(),
             "first_name": "Jimmy",
             "age": "5",
             "lucky_numbers":[1]
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"] = self._generateId() if "id" not in member else member["id"]
        member["last_name"] = self.last_name
        self._members.append(member)
        pass

    def delete_member(self, id):
        # fill this method and update the return
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        return False
        pass

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
