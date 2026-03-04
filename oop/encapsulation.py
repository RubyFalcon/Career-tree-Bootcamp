class BadBankAccount:
    def __init__(self,balance):
        self.balance = balance

# account = BadBankAccount(0)
# account.balance = -1 # we can set to a negative number
# print(account.balance) #not ideal

class BankAccount:
    def __init__(self):
        self._balance = 0.0
    # Encapsulate balance attribute inside class = inaccessable outside of the class

    # use property for getters in python
    @property
    def balance(self):
        return self._balance

    # in order to modify balance, we either use deposit or withdraw, so no setter
    def desposit(self, amount):
        if amount <=0:
            raise ValueError("Amount must be positive")
        else:
            self._balance += amount
    
    def widthdraw(self,amount):
        if amount <=0:
            raise ValueError("Widthraw amount must be positive")
        elif amount > self._balance:
            raise ValueError("Insufficient funds")
        else:
            self._balance -= amount
    def __str__(self):
        return f"Your balance is £{self.balance:.2f}"


account = BankAccount()
print(account.balance)
# account.balance = -1 => not allowed 
account.desposit(100)
print(account.balance)
account.widthdraw(.01)
print(account)
