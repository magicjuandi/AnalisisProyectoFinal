from SpellMediator import SpellMediator
from Spell import Spell
from Wizard import Wizard
if __name__ == "__main__":
    mediator = SpellMediator()
    fireball_spell = Spell("Fireball")
    heal_spell = Spell("Heal")

    mediator.register_spell("fireball", fireball_spell)
    mediator.register_spell("heal", heal_spell)

    gandalf = Wizard("Gargamel", mediator)
    gandalf.cast_spell("fireball")
    gandalf.cast_spell("heal")