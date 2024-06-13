from Wizard import Wizard
from SpellProxy import SpellProxy
if __name__ == "__main__":
    wizard1 = Wizard("Gandalf")
    wizard2 = Wizard("Harry")

    proxy_spell = SpellProxy("Fireball")
    proxy_spell.cast(wizard1)  
    proxy_spell.cast(wizard2)  