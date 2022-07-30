# Write a class called BankAccount that has the following:

# • A field called 'name' that stores the name of the account holder. • A field called amount that stores the amount of money in the account. • A field called interest rate that stores the account's interest rate (as a percentage). • A constructor that just sets the values of the three fields above.

# • A method called apply_interest() that takes no arguments and applies the interest to the account. It should just modify the amount field and not return anything. For instance, if the account has $1000 in it and the interest rate is 3%, then the amount variable should be changed to $1030 ($1000 + 3% interest). Then test the class, by creating a new BankAccount object for a user named Juan De Hattatime who has $1000 at 3% interest. Then do the following:

# • Use the apply_interest() method to apply the interest to the account. • Print out how much money is now in the account after applying the interest. • Change the account's interest rate to 2%. • Use the apply_interest() method to apply the interest to the account again. • Print out how much money is now in the account after applying the interest again.

class BankAccount:
    def __init__(self, name, amount, interestRate):
        self.name = name
        self.amount = amount
        self.interestRate = interestRate

    def apply_interest(self):
        self.amount *= (1+self.interestRate/100)


account = BankAccount('Juan De Hattatime', 1000, 3)
print(account.name)
print(account.amount)
print(account.interestRate)
account.apply_interest()
print(account.amount)
account.interestRate = 2
account.apply_interest()
print(account.amount)
print(account.interestRate)
