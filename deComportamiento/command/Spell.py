class Spell:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Spell '{self.name}' is executed.")