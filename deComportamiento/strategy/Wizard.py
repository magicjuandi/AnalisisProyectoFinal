class Wizard:
    def __init__(self, strategy):
        self._strategy = strategy

    def cast_spell(self):
        self._strategy.cast_spell()

    def set_strategy(self, strategy):
        self._strategy = strategy