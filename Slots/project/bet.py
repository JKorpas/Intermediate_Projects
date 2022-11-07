MIN_BET = 1
MAX_BET = 100


class Bet:
    def __init__(self, bet) -> None:
        self._bet = bet

    @property
    def bet(self):
        return f"Your's deposit: {self._bet}"

    @bet.setter
    def bet(self, value):
        if MIN_BET <= value <= MAX_BET:
            self._bet = value
        else:
            raise ValueError("Please enter price higher than 0")

    def show_bet(self):
        return self._bet
