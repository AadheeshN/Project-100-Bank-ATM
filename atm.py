class ATM():
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number
    
    
    def cashWithdrawal(self):
        print("You have Successfully Withdrawn Money from your Account!", self.card_number)
    

    def balanceEnquiry(self):
        print("We're Processing your Account", self.card_number)


def main():
    userOne = ATM("867592", "192837")
    userOne.cashWithdrawal()
    userOne.balanceEnquiry()
    userTwo = ATM("549876", "564738")
    userTwo.cashWithdrawal()
    userTwo.balanceEnquiry()

    
main()