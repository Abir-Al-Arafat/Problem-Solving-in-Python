# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.

# Create a constructor with parameters: accountNumber, name, balance.

# Create a deposit() method which manages the deposit actions.

# Create a withdrawal() method which manages withdrawals actions. it should show the balance after withdrawal. If the balance is less than the witdrawal amount, then the method should notice the client as 'Insufficent account'.

# Create a bankFees() method to apply the bank fees with a percentage of 5% of the balance account.

# Create a display() method to display account details.

# Give the complete code for the BankAccount class.

class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def deposit(self, depositAmount):
        self.balance += depositAmount

    def withdrawal(self, withdrawAmount):
        if self.balance > withdrawAmount:
            self.balance -= withdrawAmount
            return f'Balance after withdrawal {self.balance}'
        return 'insufficient balance'

    def bankFees(self):
        if self.balance:
            fees = (self.balance/100)*5
            self.balance -= fees
            return f'Fees: {fees}\nNew Balance: {self.balance}'

    def display(self):
        print('Account Number:', self.accountNumber)
        print('Name:', self.name)
        print('Balance:', self.balance)


account = BankAccount(2203220, 'Joe', 1001)
account.deposit(20)
print(account.withdrawal(1))
account.display()

print(account.bankFees())
account.display()
