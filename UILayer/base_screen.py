class BaseScreen:
    def __init__(self, ui):
        self.ui = ui

    def render(self):
        raise NotImplementedError("Subclass needs to implement render()")
