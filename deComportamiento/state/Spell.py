class Spell:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def cast(self):
        self._state.cast()