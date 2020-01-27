#!/usr/bin/python3

from datetime import date,timedelta

OVERDRAFT_FEE = float(10.0)
MIN_RATE = float(1.0)
MAX_RATE = float(2.0)

class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance 
        self.last_interest_date = date.today()
        self.rate = 0.0

    def deposit(self, amount):
        if(amount >= 0 ):
            self.balance += amount
        else:
            print(f"amount: {amount} is invalid")
        return self.balance

    def withdraw(self, withdrawal):
        if(self.balance - withdrawal < 0):
            self.balance = self.balance - withdrawal - OVERDRAFT_FEE
            print('insuffecient funds, charged $10 overdraft fee')
        else:
            self.balance -= withdrawal
            print(f'withdrawal of ${withdrawal} successful')

    def add_interest(self, added_interest, test_date = date.today()):
        is_30_days =  self.last_interest_date + timedelta(days = 30)

        if(self.balance > 0 
        and added_interest >= MIN_RATE 
        and added_interest <= MAX_RATE
        and date.today() >= is_30_days):
            self.rate += added_interest
            print(f'%{added_interest} interest added')
        else:
            print("did not add interest (with today's date): ",date.today())
            
        if(test_date >= is_30_days
        and added_interest >= MIN_RATE 
        and added_interest <= MAX_RATE
        and self.balance > 0):
            self.rate += added_interest
            print(f'%{added_interest} interest added (with a mock date): ',test_date)
        else:
            print("did not add interest (with a mock date): ",test_date)

        return self.rate
            
    def get_balance(self):
        return self.balance


# account = BankAccount(1000);
# account.deposit(10)
# print(account.get_balance())
