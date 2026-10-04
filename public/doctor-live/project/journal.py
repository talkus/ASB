"""Journal local. verify_chain ne scelle pas un WORM absent."""

class Journal:
    def __init__(self):
        self.entries = []

    def verify_chain(self):
        return False
