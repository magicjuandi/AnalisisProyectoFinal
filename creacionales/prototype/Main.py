from Spell import Spell
if __name__ == "__main__":
    original_spell = Spell("Heal", ["Restore Health"])
    cloned_spell = original_spell.clone()
    cloned_spell.effects.append("Remove Poison")

    print(original_spell)
    print(cloned_spell)