class FamilyMember:
    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.parents = []
        self.children = []

    def add_parent(self, parent):
        self.parents.append(parent)
        parent.children.append(self)

    def add_child(self, child):
        self.children.append(child)
        child.parents.append(self)

    def __str__(self):
        return f"{self.name} ({self.gender}, {self.birth_year})"
