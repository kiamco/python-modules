#!/usr/bin/python3


"""
Instantiate a bank account with an original balance of $1000.00
Deposit $500.00
Withdraws $2000.00
Adds 1% interest 
Adds  2% interest
Deposit $125,000.99
Withdraws $0.99
Withdraws $126,500.00
Withdraws $10.00
Adds 1% interest
"""
from kimkiamcoBank import BankAccount
from datetime import date, timedelta

## create new account
print('creating new account.. ')
account = BankAccount(1000)

print(f'account made with balance of  ${account.get_balance()} \n')

print(f'depositing $500 ...')
account.deposit(500)
print(f'current balance: {account.get_balance()}\n')

print('adding %1 rate')
print(f'last interest date on account: {account.last_interest_date}')
mock_date = date.today() + timedelta(days = 31)
print(f'mock date will be {mock_date}')
account.add_interest(1,mock_date)
print(f'account interest: %{account.rate}\n')

print('adding %2 rate')
print(f'last interest date on account: {account.last_interest_date}')
mock_date = date.today() + timedelta(days = 31)
print(f'mock date will be {mock_date}')
account.add_interest(2,mock_date)
print(f'account interest: %{account.rate}\n')

print(f'depositing $125,000.99 ...')
account.deposit(125000.99)
print(f'current balance: {account.get_balance()}\n')

print("withdrawing $0.99 ...")
account.withdraw(0.99)
print(f'current balance: {account.get_balance()}\n')

print("withdrawing $0.99 ...")
account.withdraw(126500.00)
print(f'current balance: {account.get_balance()}\n')

print("withdrawing $10.00 ...")
account.withdraw(10)
print(f'current balance: {account.get_balance()}\n')

print('adding %1 rate')
print(f'last interest date on account: {account.last_interest_date}')
mock_date = date.today() + timedelta(days = 31)
print(f'mock date will be {mock_date}')
account.add_interest(1,mock_date)
print(f'account interest: %{account.rate}\n')
