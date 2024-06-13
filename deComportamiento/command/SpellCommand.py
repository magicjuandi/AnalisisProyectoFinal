class SpellCommand:
    def __init__(self, spell):
        self.spell = spell

    def execute(self):
        self.spell.execute()