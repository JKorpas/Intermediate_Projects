import random

from deposit import Deposit
from lines import Lines
from bet import Bet
from machine import Machine

ROWS = 3
WHEELS = 3

SYMBOL_COUNTS = {
    "$": 2,
    "@": 3,
    "#": 4,
}


if __name__ == "__main__":
    slot = Machine()
    player_depo = int(input("How much would you like to deposit?: "))
    deposit = Deposit(player_depo)
    while True:
        player_bet = int(input("How much would you like to bet?: "))
        bet = Bet(player_bet)
        player_lines = int(input("On how many lines would you like to bet?: "))
        lines = Lines(player_lines)
        total_bet = lines._lines * bet._bet
        if total_bet < deposit._deposit:
            print(f"Your total bet is equal to: {total_bet}$")
            slot.get_spin(ROWS, WHEELS, SYMBOL_COUNTS)
        else:
            print(f"Not enough money. Your current balance is {deposit._deposit}$")
            while True:
                add_depo_or_change_bet = str(
                    input("Would u like to (i)ncrease depo or (r)e-bet?: ").lower()
                )
                if add_depo_or_change_bet == "i":
                    player_depo = int(
                        input("How much would you like to add to your deposit?: ")
                    )
                    deposit.increase_deposit(player_depo)
                    print(f"Your current deposit is equalt to: {deposit._deposit}$")
                    break
                elif add_depo_or_change_bet == "r":
                    break
                else:
                    print("enter your answer correctly")
                    continue
            continue
