from BaseSpell import BaseSpell
from IceSpell import IceSpell
from FireSpell import FireSpell
if __name__ == "__main__":
    base_spell = BaseSpell()
    fire_spell = FireSpell(base_spell)
    ice_spell = IceSpell(base_spell)

    base_spell.cast()
    fire_spell.cast()
    ice_spell.cast()