class MagicItemBridge:
    def __init__(self, magic_item):
        self.magic_item = magic_item

    def apply(self):
        self.magic_item.apply()
