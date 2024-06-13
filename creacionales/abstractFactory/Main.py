from HealingMagicFactory import HealingMagicFactory
if __name__ == "__main__":
    factory = HealingMagicFactory()
    spell = factory.create_spell()
    potion = factory.create_potion()

    print(spell)
    print(potion)