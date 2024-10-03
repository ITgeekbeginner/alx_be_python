class BankAccount:
    def __init__(self, initial_balance=100):
        self._account_balance = initial_balance

    def deposit(self ,amount):
       if amount > 100:
          amount = self._account_balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
             amount = self._account_balance -amount
             print("Withdrew: ${amount}")
        
        
    
    
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

BankAccount()