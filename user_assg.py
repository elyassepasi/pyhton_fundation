class User:
    def __init__(self,username,email):
        self.name=username
        self.email=email
        self.account_balance=0

    def make_deposit(self, amount): #deposit money adds to account balance
        self.account_balance += amount
        
    def make_withdrawal(self, amount): #withdraw money deducts from account balance
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: "+self.name+", Balance: ",self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount 
        # self.other_name= other_user 
        print("Other user: "+other_user+", Other balance: ",amount)
        print("User: "+self.name+", Balance: ",self.account_balance)
        
        


Glid= User("Glid Sky","GS@com")
#print('Name: '+Glid.name+',','Email: ' +Glid.email)

dark= User("Dark D", "DD@com")

Glid.make_deposit(100)
# print(Glid.account_balance)

Glid.make_withdrawal(50)
# print(Glid.account_balance)

Marg= User("Marg","MJ@com")
#print(Marg.name)
Marg.make_deposit(1000)
print("Marg has","$",Marg.account_balance)

Glid.display_user_balance()
Marg.transfer_money("Jak", 200)
# print(Glid.transfer_money)



