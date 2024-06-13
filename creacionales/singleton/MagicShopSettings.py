class MagicShopSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MagicShopSettings, cls).__new__(cls)
            cls._instance.settings = {}
        return cls._instance