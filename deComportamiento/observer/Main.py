from Wizard import Wizard
from SpellBook import SpellBook
if __name__ == "__main__":
    spell_book = SpellBook()

    gandalf = Wizard("Gandalf")
    harry = Wizard("Harry")

    spell_book.add_observer(gandalf)
    spell_book.add_observer(harry)

    spell_book.new_spell("Fireball")