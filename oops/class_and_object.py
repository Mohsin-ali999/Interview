
class Bank_Account:
    def __init__(self,name,balance=0):
        self.name= name
        self.balance= balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        

    def deposit(self, amount):
        self.balance += amount


a1 = Bank_Account('Mohsin', 300)
a2 = Bank_Account('Bilal', 500)

a1.display()
a2.display()

a1.withdraw(100)
a2.withdraw(200)

a1.display()
a2.display()