from Spell import Spell
from SpellBook import SpellBook
if __name__ == "__main__":
    spell1 = Spell("Fireball")
    spell2 = Spell("Heal")

    spell_book = SpellBook()
    spell_book.add_spell(spell1)
    spell_book.add_spell(spell2)

    spell_book.display()