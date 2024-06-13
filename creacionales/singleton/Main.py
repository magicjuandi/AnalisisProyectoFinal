from MagicShopSettings import MagicShopSettings
if __name__ == "__main__":
    settings1 = MagicShopSettings()
    settings2 = MagicShopSettings()

    settings1.settings["opening_hours"] = "9:00 AM"
    print(settings2.settings["opening_hours"]) 