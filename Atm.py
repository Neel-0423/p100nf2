class Atm():
    def __init__(self,acn,pn,amt):
        self.acn=acn
        self.amt =amt
        self.pn=pn
    def balanceEnquiry(self):
        print("your balance is "+ self.amt)
    def cashWithdrawl(self):
        wa = input("what ammount do you want to withdraw")
        self.amt = self.amt - wa
        print("withdrawl complete")
        print(self.amt)
def play():
    person=Atm("45776834","5732","100000")
    person.balanceEnquiry()
    person.cashWithdrawl()
    print("your account number is "+person.acn)
    print("your pin number is "+person.pn)
play()



