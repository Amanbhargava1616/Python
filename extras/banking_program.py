class Banking:
    def __init__(self, deposit: int) -> None:
        if deposit <= 0:
            raise ValueError(f"Initial Deposit should be greater than zero")
        self._balance = deposit

    @property
    def balance(self):
        return self._balance

    def deposit(self, amt: int) -> None:
        if amt <= 0:
            raise ValueError(f"Amt to be deposited should be greater than zero")

        self._balance += amt
        print(f"Amount {amt} deposited, current balance {self.balance}.")

    def withdraw(self, amt: int) -> None:
        if amt > self._balance:
            msg = f"Amt to be withdrawn should not be greater than balance {self.balance}"
            raise ValueError(msg)

        self._balance -= amt
        print(f"Amount {amt} withdrawn, remaining balance {self.balance}.")


def main() -> None:
    bank = Banking(deposit=100)
    # bank.deposit(amt=-10)
    bank.deposit(amt=50)
    # bank.withdraw(amt=200)
    bank.withdraw(amt=80)
    print(f"Current Balance: {bank.balance}")


if __name__ == "__main__":
    main()
