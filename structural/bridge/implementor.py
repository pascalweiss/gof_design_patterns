

# --- Implementor ---

class Renderer:
    _separator = " #"

    def render(self, txt):
        raise NotImplementedError


# --- Concrete Implementor ---

class Paper(Renderer):
    def render(self, txt):
        return txt + self._separator + " on paper"


class Audio(Renderer):
    def render(self, txt):
        return txt + self._separator + " in audio"


class Web(Renderer):
    def render(self, txt):
        return txt + self._separator + " in html"
