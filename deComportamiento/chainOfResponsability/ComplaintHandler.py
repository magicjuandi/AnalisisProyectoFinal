class ComplaintHandler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_complaint(self, complaint):
        if self._successor:
            self._successor.handle_complaint(complaint)