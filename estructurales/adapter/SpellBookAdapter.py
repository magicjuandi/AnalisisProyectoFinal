from Wizard import Wizard
class SpellBookAdapter(Wizard):
    def __init__(self, spell_book):
        self.spell_book = spell_book

    def cast_spell(self, spell_name):
        spell_description = self.spell_book.get_spell(spell_name)
        if spell_description != "Unknown spell":
            print(f"Wizard casts '{spell_description}'.")
        else:
            print(f"Wizard doesn't know '{spell_name}'.")