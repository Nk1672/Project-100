class Atm(object):

    def __init__(self,pinNumber,cardNumber,ammount,balenceLimit):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        
    def cashWithdraw():
        print("Successfully Withdrew!")

    def cashDeposit():
        print("Successfully Deposited!")

    def balenceEnquiry():
        print("You have $2638 deposited")

myAtm = Atm("Nirvik","6729371","82683648264","2638","2000")

