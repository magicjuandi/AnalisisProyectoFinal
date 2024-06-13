from IceSpellState import IceSpellState
from FireSpellState import FireSpellState
from Spell import Spell
if __name__ == "__main__":
    spell = Spell()
    fire_state = FireSpellState()
    ice_state = IceSpellState()

    spell.set_state(fire_state)
    spell.cast()

    spell.set_state(ice_state)
    spell.cast()