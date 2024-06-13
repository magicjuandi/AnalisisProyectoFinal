from HealSpell import HealSpell
from FireBallSpell import FireBallSpell
if __name__ == "__main__":
    fireball_spell = FireBallSpell()
    fireball_spell.prepare_materials()
    fireball_spell.perform_ritual()
    fireball_spell.complete()

    heal_spell = HealSpell()
    heal_spell.prepare_materials()
    heal_spell.perform_ritual()
    heal_spell.complete()