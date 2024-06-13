from Wizard import Wizard
from Spell import Spell
from SpellCommand import SpellCommand
if __name__ == "__main__":
    wizard = Wizard()
    spell = Spell("Fireball")
    command = SpellCommand(spell)

    wizard.cast_spell(command)