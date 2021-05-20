class BankAccount:
    def __init__(self,interst_rate,balance):
        self.interst_rate=interst_rate
        self.account_balance=balance
        self.total_balance=0
        self.interst=0
    
    def deposit(self, amount):
        self.account_balance += amount
        
        return self

        
    def withdrawal(self,amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            self.account_balance -=5
            print("Insufficient funds: Charging a $5 fee. Your balance is: $",self.account_balance+5, "and your total is: ", self.account_balance)
        
        return self

    def display_account_info(self):
        self.total_balance = self.interst_rate * self.account_balance + self.account_balance
        print("Balance:", self.total_balance)


    def yield_interest(self):
        if self.account_balance>0:
            self.interst=self.account_balance*self.interst_rate
            print("yout have gained",self.interst,"intrest")
        return self

first_account= BankAccount(0.04,1000)
second_account= BankAccount(0.04,500)

first_account.deposit(4000).deposit(500).withdrawal(1000).yield_interest().display_account_info()
second_account.deposit(5000).deposit(500).withdrawal(1000).withdrawal(2500).withdrawal(10).withdrawal(3000).yield_interest().display_account_info()
