# This is creating a bank with checking and savings accounts
# Checking accounts have a min_balance of -$200 with overdraft protection
# Saving accounts have minimum balance of $0


class Account:

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('Sorry, not enough money in your account, {}!'.format(self.name))

    def statement(self):
        print('Account Balance: ${}'.format(self.balance))

    # below is a method telling what to print to console when printing an account. ex: print(mike_account)
    def __str__(self):

        return "{}'s Current Account Balance: ${}".format(self.name, self.balance)


class Checking(Account):

    # must enter self, name balance to create a checking account
    def __init__(self, name, balance):

        # below passes name and balance into Account class with super() method to get values for object
        super().__init__(name, balance, min_balance=-200)


class Saving(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)


mike_account = Saving('Mike', 250000)
print(mike_account)

mike_account.withdraw(300)
print(mike_account)

mike_account.deposit(1511)
print(mike_account)

mike_account.withdraw(1000000)

jessi_account = Checking('Jessi', 500)
jessi_account.withdraw(100)
jessi_account.deposit(500)
print(jessi_account)