class Spell:
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super(Spell, cls).__new__(cls)
            cls._instances[name].name = name
        return cls._instances[name]