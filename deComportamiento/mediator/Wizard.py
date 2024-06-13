class Wizard:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def cast_spell(self, spell_name):
        self.mediator.cast_spell(spell_name, self)