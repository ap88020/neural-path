class BankAccount:
    def __init__(self,name,balance):
        self.name = name #Public
        # self._balance = balance #Protected
        self.__balance = balance #Private

    def get_balance(self):
        return self.__balance
    
    def set_balance(self,newBalance):
        self.__balance = newBalance


acc1 = BankAccount("Akash Patel",100000)
acc1.set_balance(200000)
print(acc1.name , acc1._BankAccount__balance)