from family_member import FamilyMember

class FamilyTree:
    def __init__(self):
        self.members = {}

    def add_member(self, name, gender, birth_year):
        if name not in self.members:
            member = FamilyMember(name, gender, birth_year)
            self.members[name] = member
            print(f"Added {member}")
        else:
            print(f"Member {name} already exists.")

    def add_relationship(self, parent_name, child_name):
        if parent_name in self.members and child_name in self.members:
            parent = self.members[parent_name]
            child = self.members[child_name]
            parent.add_child(child)
            print(f"Added relationship: {parent_name} -> {child_name}")
        else:
            print(f"One or both members not found: {parent_name}, {child_name}")

    def display_member(self, name):
        if name in self.members:
            member = self.members[name]
            print(f"Name: {member.name}")
            print(f"Gender: {member.gender}")
            print(f"Birth Year: {member.birth_year}")
            print("Parents:", ", ".join([parent.name for parent in member.parents]) or "None")
            print("Children:", ", ".join([child.name for child in member.children]) or "None")
        else:
            print(f"Member {name} not found.")

    def display_all_members(self):
        if not self.members:
            print("No members in the family tree.")
        for name, member in self.members.items():
            self.display_member(name)
            print("-" * 20)
