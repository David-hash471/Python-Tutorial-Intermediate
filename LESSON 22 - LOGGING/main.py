import os
import logging
from logging.handlers import RotatingFileHandler


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount > 0:
            self.balance -= amount


def setup_logging(log_file, log_dir='logs'):
    pass


def main():
    setup_logging('bank.log')
    acc = BankAccount('Bob', 100)
    acc.deposit(40)
    acc.withdraw(20)
    acc.withdraw(150)
    acc.deposit(-10)


if __name__ == '__main__':
    main()
