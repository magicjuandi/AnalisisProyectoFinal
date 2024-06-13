from Ring import Ring
from Wand import Wand
from MagicItemBridge import MagicItemBridge
if __name__ == "__main__":
    wand = Wand("Fire")
    ring = Ring("Protection")

    wand_bridge = MagicItemBridge(wand)
    ring_bridge = MagicItemBridge(ring)

    wand_bridge.apply()
    ring_bridge.apply()
