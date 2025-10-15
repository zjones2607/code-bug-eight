class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount): #missing self parameter
        if amount <= 0: # Added check for non-positive deposit amounts
            print("Deposit amount must be positive")
            return
        self.balance += amount # Fixed typo from =+ to +=
        print(f"Deposited ${amount}. New balance is ${self.balance}") #cooncatenation fixed

    def withdraw(self, amount):
        if amount <= 0: # Added check for non-positive withdrawal amounts
            print("Withdrawal amount must be positive")
            return
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}")

    def display_balance():
        print(f"{self.owner}'s account balance: ${self.balance}")

# Create an account
account = BankAccount("Alice", 1000)

# Perform transactions
account.deposit(200)
account.withdraw(150)
account.display_balance()