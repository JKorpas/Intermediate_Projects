MIN_LINES = 1
MAX_LINES = 5


class Lines:
    def __init__(self, lines) -> None:
        self._lines = lines

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        if 1 <= value <= MAX_LINES:
            self._lines = value
        else:
            raise ValueError(
                "Please enter integer value between {MIN_LINES} and {MAX_LINES} ")

    def show_lines(self):
        return self._lines
