class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate =int_rate
        self.balance =balance
        
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient funs:charging a $5 fee {self.balance-5}")
        else:
            self.balance -= amount
        return self
    def display(self):
        print(f"Balance: {self.balance}")
        return self
    
    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self


account1 = BankAccount(.15,5000)
account2 = BankAccount(.10, 4000)


#  To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)

account1.deposit(500).deposit(500).deposit(500).withdraw(400).yield_interest().display()


# To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)

account2.deposit(100).deposit(100).withdraw(500).withdraw(300).withdraw(400).withdraw(4000).yield_interest().display()

