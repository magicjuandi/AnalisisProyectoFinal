from SpellBook import SpellBook
from SpellBookAdapter import SpellBookAdapter
if __name__ == "__main__":
    spell_book = SpellBook()
    wizard = SpellBookAdapter(spell_book)

    wizard.cast_spell("fireball")
    wizard.cast_spell("heal")
    wizard.cast_spell("ice")