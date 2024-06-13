class WizardVisitor:
    def visit_fire_spell(self, spell):
        print(f"Wizard casts fire spell: {spell}")

    def visit_heal_spell(self, spell):
        print(f"Wizard casts heal spell: {spell}")
