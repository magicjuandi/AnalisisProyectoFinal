class Spell:
    def __init__(self, name):
        self.name = name
        self._state = None

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state