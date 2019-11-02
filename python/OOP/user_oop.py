

class User():
    def __init__(self,first_name,last_name,account_balance):
        self.first_name =first_name
        self.last_name = last_name
        self.account_balance = account_balance

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawl(self,amount):
        self.account_balance -=amount


    def display_user_balance(self):
        print(f'User: {self.first_name}{self.last_name} Balance:{self.account_balance}')

    def transfer_money(self,from_acc,to_acco,amount):
        from_acc.make_withdrawl(amount)
        to_acco.make_deposit(amount)




user1 = User('pramila','gharti',1500)
user2 = User ('sirish','shrestha',6000)
user3 = User('sita','magar',9000)
user1.make_deposit(500)
user1.make_deposit(500)
user1.make_deposit(500)
user1.make_withdrawl(500)
user1.display_user_balance()

user2.make_deposit(1000)
user2.make_deposit(1000)
user2.make_withdrawl(500)
user2.make_withdrawl(500)
user2.display_user_balance()

user3.make_deposit(1000)
user3.make_withdrawl(1000)
user3.make_withdrawl(1000)
user3.make_withdrawl(1000)
user3.display_user_balance()
print('-------------------')

user1.transfer_money(user1,user3,1000)
user1.display_user_balance()
user3.display_user_balance()