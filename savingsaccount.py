class SavingsAccount():
    def __init__(self,accnum,name,balance = 0,depositamount = 0, withdrawlamount = 0):
        self.accnum = accnum
        self.name = name
        self.balance = balance
        self.depositamount = depositamount
        self.withdrawlamount = withdrawlamount

    def Show(self):
        print(self.accnum)
        print(self.name)
        print(self.GetBalance())

    def Withdrawl(self,amount):
        self.withdrawlamount = self.withdrawlamount+amount

    def Deposit(self,amount):
        self.depositamount = self.depositamount+amount


    def GetBalance(self):
        return self.balance + self.depositamount-self.withdrawlamount


KavyaAccount = SavingsAccount(123,"Kavya",1000)
KavyaAccount.Deposit(50)

KeerthiAccount = SavingsAccount(456,"Keerthi",2)

KrupaAccount = SavingsAccount(789,"Krupa",100)
KrupaAccount.Withdrawl(30)
KavyaAccount.Show()
KrupaAccount.Show()
KeerthiAccount.Show()