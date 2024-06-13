from SpellBuilder import SpellBuilder

if __name__ == "__main__":
    builder = SpellBuilder()
    spell = (builder.set_name("Fireball")
                    .add_effect("Damage")
                    .set_level(3)
                    .build())

    print(spell)