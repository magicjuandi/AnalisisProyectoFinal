from MagicItem import MagicItem
class Ring(MagicItem):
    def apply(self):
        print(f"Ring applies {self.name} effect.")