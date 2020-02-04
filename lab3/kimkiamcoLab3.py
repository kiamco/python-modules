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


"""
creating new account..
account made with balance of  $1000

depositing $500 ...
current balance: 1500

adding %1 rate
last interest date on account: 2020-01-28
mock date will be 2020-02-28
did not add interest (with today's date):  2020-01-28
%1 interest added (with a mock date):  2020-02-28
account interest: %1.0

adding %2 rate
last interest date on account: 2020-01-28
mock date will be 2020-02-28
did not add interest (with today's date):  2020-01-28
%2 interest added (with a mock date):  2020-02-28
account interest: %3.0

depositing $125,000.99 ...
current balance: 126500.99

withdrawing $0.99 ...
withdrawal of $0.99 successful
current balance: 126500.0

withdrawing $0.99 ...
withdrawal of $126500.0 successful
current balance: 0.0

withdrawing $10.00 ...
insuffecient funds, charged $10 overdraft fee
current balance: -20.0

adding %1 rate
last interest date on account: 2020-01-28
mock date will be 2020-02-28
did not add interest (with today's date):  2020-01-28
did not add interest (with a mock date):  2020-02-28
account interest: %3.0
"""
