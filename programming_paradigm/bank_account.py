class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self ,amount):
       if amount > 0:
          amount = self._account_balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
             amount = self._account_balance -amount
             print("Withdrawn: ${amount}")
        else:
            print("Insufficient funds")
        
    
    
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

BankAccount()