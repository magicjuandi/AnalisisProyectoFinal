from Observer import Observer
class Wizard(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, spell):
        print(f"{self.name} received new spell: {spell}")
