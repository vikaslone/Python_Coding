'''
For this challenge, create a bank account class that has two attributes:
owner
balance

and two methods:
deposit
withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
    pass

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)
Account owner:   Jose
Account balance: $100

# 3. Show the account owner attribute
acct1.owner

'Jose'

# 4. Show the account balance attribute
acct1.balance

100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
Deposit Accepted

acct1.withdraw(75)
Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)

Funds Unavailable!
'''

class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f'{deposit_amount} has been deposited and the new balance is {self.balance}')

    def withdraw(self, withdraw_am):
        if self.balance == 0:
            print('Funds Unavailable')
        elif self.balance < withdraw_am:
            print('Withdrawal amount greater than existing account balance')
        else:
            self.balance -= withdraw_am
            print(f'{withdraw_am} has been withdrawn and available balance is {self.balance}')
    
    def __str__(self):
        return (f'Account owner {self.owner} has balance of {self.balance}')

ac1 = Account('Guest1', 100)

print(ac1)

ac1.deposit(400)

ac1.withdraw(100)

print(ac1)

ac1.withdraw(600)