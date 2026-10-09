from random import choices
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

# Domain types
type SlotSymbol = Literal["A", "B", "C"]
type RollType = tuple[SlotSymbol, SlotSymbol, SlotSymbol]

SLOT_OPTIONS: tuple[SlotSymbol, ...] = ("A", "B", "C")


# Result of a single bet
@dataclass(frozen=True, kw_only=True)
class RollOutput:
    roll: RollType
    multiplier: int


# Rolling abstraction
class Roller(ABC):
    @abstractmethod
    def roll(self) -> RollType: ...


class RandomRoller(Roller):
    def roll(self) -> RollType:
        x, y, z = choices(SLOT_OPTIONS, k=3)
        return x, y, z


class FakeRoller(Roller):
    """Deterministic roller for unit tests."""

    def __init__(self, rolled: RollType) -> None:
        self._rolled = rolled

    def roll(self) -> RollType:
        return self._rolled


# Payout rules
class PayoutCalculator:

    def calculate(self, roll: RollType) -> int:
        unique_count = len(set(roll))
        if unique_count == 1:
            return 10
        elif unique_count == 2:
            return 7 if roll[0] == roll[1] else 4
        else:
            return -1


# Core game logic
class LuckyLemons:
    def __init__(
        self,
        base_amount: int,
        roller: Roller,
        payout_calculator: PayoutCalculator,
    ) -> None:
        self._validate_base_amount(base_amount)

        self._balance = base_amount
        self._roller = roller
        self._payout_calculator = payout_calculator

    @property
    def balance(self) -> int:
        return self._balance

    def add_funds(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")

        self._balance += amount

    def bet(self, bet_amount: int) -> RollOutput:
        self._validate_bet(bet_amount)

        roll = self._roller.roll()
        multiplier = self._payout_calculator.calculate(roll)

        self._balance += multiplier * bet_amount

        return RollOutput(roll=roll, multiplier=multiplier)

    def _validate_bet(self, bet_amount: int) -> None:
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than 0")

        if self._balance <= 0:
            raise ValueError("Your balance is 0; please add funds to bet")

        if bet_amount > self._balance:
            raise ValueError(f"Bet amount cannot be greater than your balance ({self._balance})")

    @staticmethod
    def _validate_base_amount(base_amount: int) -> None:

        if base_amount < 0:
            raise ValueError("Base amount cannot be negative")


# CLI helpers
def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


# CLI entry point
def main() -> None:
    menu = """
Select an operation:
1. Add funds
2. Bet
Press Enter to exit.
"""

    roller = RandomRoller()
    payout_calculator = PayoutCalculator()

    while True:
        base_amount = read_integer("Enter base amount: ")

        try:
            game = LuckyLemons(
                base_amount=base_amount,
                roller=roller,
                payout_calculator=payout_calculator,
            )
            break
        except ValueError as exc:
            print(exc)
        except TypeError as exc:
            print(exc)

    print(f"Opening balance: {game.balance}")

    while True:
        operation = input(menu).strip()

        if not operation:
            print("Goodbye!")
            break

        if operation not in ("1", "2"):
            print("Please select either 1 or 2.")
            continue

        amount = read_integer("Enter amount: ")

        try:
            if operation == "1":
                game.add_funds(amount)
                print(f"Current balance: {game.balance}")

            else:
                result = game.bet(amount)
                print(f"You rolled: {result.roll}")
                print(f"Multiplier: {result.multiplier}")
                print(f"Current balance: {game.balance}")

        except ValueError as exc:
            print(exc)


if __name__ == "__main__":
    main()
