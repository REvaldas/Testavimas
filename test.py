import pytest
from bank import BankAccount

def test_deposit():
    acc = BankAccount("Simonas", 100)
    assert acc.deposit(50) == 150
    with pytest.raises(ValueError):
        acc.deposit(-10)

def test_withdraw():
    acc = BankAccount("Gabija", 100)
    assert acc.withdraw(50) == 50
    with pytest.raises(ValueError):
        acc.withdraw(333)  # not enough funds
    with pytest.raises(ValueError):
        acc.withdraw(-20)
