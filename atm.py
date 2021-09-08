class ATM(object):
    def __init__(self,cardNo,pinNo):
        self.cardNo=cardNo
        self.pinNo=pinNo
 
    def CashWithdrawn(self,object):
        print("Cash Withdrawn:",object)

    def BalanceEnquiry(self,object):
        print("Balance is:",object)

Raama=ATM("4660 7703 2825 7291","1328")
print("Raama's card #:",Raama.cardNo)
print("Raama's pin #:",Raama.pinNo)
Raama.CashWithdrawn(1230.38)
Raama.BalanceEnquiry(5010.42)