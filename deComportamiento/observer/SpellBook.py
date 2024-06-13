class SpellBook:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, spell):
        for observer in self._observers:
            observer.update(spell)

    def new_spell(self, spell):
        self.notify_observers(spell)