from MagicShopFacade import MagicShopFacade
if __name__ == "__main__":
    shop = MagicShopFacade()
    shop.create_spell("Fireball", 10)
    shop.create_spell("Heal", 8)

    shop.show_spell_list()