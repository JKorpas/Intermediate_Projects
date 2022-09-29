MAX_DEPOSIT = 1000
MIN_DEPOSIT = 1


class Deposit:
    def __init__(self, deposit) -> None:
        self._deposit = deposit

    @property
    def deposit(self):
        return f"Your's deposit: {self._deposit}"

    @deposit.setter
    def deposit(self, value):
        if MIN_DEPOSIT <= value <= MAX_DEPOSIT:
            self._deposit = value
        else:
            raise ValueError(
                f"Please enter positive integer value between {MIN_DEPOSIT} and {MAX_DEPOSIT} ")

    def show_deposit(self):
        return self._deposit

    def increase_deposit(self, value):
        if MIN_DEPOSIT <= value <= MAX_DEPOSIT:
            self._deposit += value
        else:
            raise ValueError(
                f"Please enter positive integer value between {MIN_DEPOSIT} and {MAX_DEPOSIT} ")
        