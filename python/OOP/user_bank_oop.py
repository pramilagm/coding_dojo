class BankAccount:

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    
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



class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.checking_account = BankAccount(int_rate = .02,balance=0)
        self.saving_account = BankAccount(int_rate = .02,balance=0)

    def make_deposit(self, amount, accountType):
        if accountType == "checking":
            self.checking_account.deposit(amount)
        elif accountType == "saving":
            self.saving_account.deposit(amount)
        return self
       

    def make_withdrawl(self,amount,accountType):
        if accountType == 'checking':
            self.checking_account.withdraw(amount)
        elif accountType =='saving':
            self.saving_account.withdraw(amount)
        return self
       

    def display_user_balance(self,accountType):
        if accountType=='checking':
            print(f' User: {self.name} Balance:{self.checking_account.balance}')
        elif accountType=='saving':
            print(f'User: {self.name} Balance:{self.saving_account.balance}')



user1 = User('pramila','gharti')


user1.make_deposit(500, "checking").display_user_balance('checking')
user1.make_deposit(1000,'saving').make_withdrawl(400,'saving').display_user_balance('saving')

