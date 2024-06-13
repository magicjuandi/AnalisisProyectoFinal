class RealSpell:
    def __init__(self, name):
        self.name = name

    def cast(self, wizard):
        print(f"Real spell '{self.name}' is cast by {wizard.name}.")