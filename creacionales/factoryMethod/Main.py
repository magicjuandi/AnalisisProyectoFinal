from SpellFactory import SpellFactory
if __name__ == "__main__":
    factory = SpellFactory()
    spell = factory.create_spell("Lightning Bolt")
    print(spell)