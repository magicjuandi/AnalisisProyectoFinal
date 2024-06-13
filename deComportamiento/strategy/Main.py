from Wizard import Wizard
from FireBallStrategy import FireBallStrategy
from HealStrategy import HealStrategy

if __name__ == "__main__":
    fireball_strategy = FireBallStrategy()
    heal_strategy = HealStrategy()

    gandalf = Wizard(fireball_strategy)
    gandalf.cast_spell()

    gandalf.set_strategy(heal_strategy)
    gandalf.cast_spell()