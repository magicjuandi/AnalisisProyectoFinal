from Spell import Spell
from SpellHistory import SpellHistory
if __name__ == "__main__":
    spell = Spell("Fireball")
    spell.set_state("Powerful")

    history = SpellHistory()
    history.add_memento(spell.get_state())

    spell.set_state("Weakened")
    spell.set_state(history.get_memento(0))

    print(spell.get_state())  