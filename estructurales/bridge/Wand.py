from MagicItem import MagicItem
class Wand(MagicItem):
    def apply(self):
        print(f"Wand applies {self.name} effect.")
