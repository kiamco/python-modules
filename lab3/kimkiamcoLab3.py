#!/usr/bin/python3

from kimkiamcoBank import BankAccount
## create new account
print('creating new account.. ')
account = BankAccount(1000)

print(f'account made with balance of  ${account.get_balance()}')

print(f'depositing $500 ...')
account.deposit(500)
print(f'current balance: {account.get_balance()}')