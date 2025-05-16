class Account:
    next_acc_no=10045

    def __init__(self,name):
        self.name=name
        self.acc_no=Account.next_acc_no
        Account.next_acc_no+=1
        self.__balance=0
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"{amount} deposited.New balance: {self.__balance}")
        else:
            print("Invalid input")
    def check_balance(self):
        print(f"Account Balance: {self.__balance}")
    def withdraw(self,amount):
        print("Withdraw method not implemented for base account class.")

    def _get_balance(self):
        return self.__balance
    def _set_balance(self,amount):
        self.__balance=amount

class SavingsAccount(Account):
    def __init__(self,name,interest_rate=0.04):
        super().__init__(name)
        self.interest_rate=interest_rate

    def withdraw(self, amount):
        if amount>self.__balance():
            print("Insufficient Balance")
        else:
            self._set_balance(self._get_balance()-amount)
            print(f"{amount} withdrawn.New balance:{self._get_balance}")

    def calculate_interest(self):
        interest=self._get_balance()*self.interest_rate
        print(f"Interest: {interest}")
        return interest

class CurrentAccount(Account):
    def __init__(self,name,overdraft_limit=1000):
        super().__init__(name)
        self.overdraft_limit=overdraft_limit
    def withdraw(self,amount):
        if amount>self._get_balance+self.overdraft_limit:
            print("Withdrawl exceeds overfraft limit!!")
        else:
            self._set_balance(self._get_balance()-amount)
            print(f"{amount} withdrawn.New Balance: {self._get_balance}")
def menu():
    print("***Banking System Menu***")
    print("1.Create Savings Bank Account")
    print("2.Create a Current Account")
    print("3.Deposit")
    print("4.Withdraw")
    print("5.Check Balance")
    print("6.Calculate the interest")
    print("7.Exit")
account=None
while True:
    menu()
    c=int(input("What you want to do,please enter a number: "))
    if c==1:
        name=input("Enter your name: ")
        account=SavingsAccount(name)
        print(f"Savings Bank Account is created.Account no: {account.acc_no}")
    elif c==2:
        name=input("Enter your name: ")
        account=CurrentAccount(name)
        print(f"Current Bank Account is created.Account no: {account.acc_no}")
    elif c==3:
        if account:
            amount=float(input("Enter the amount that has to be deposited: "))
            account.deposit(amount)
        else:
            print("Create an account first")
    elif c==4:
        if account:
            amount=float(input("Enter the amount that has to withdraw: "))
            account.withdraw(amount)
        else:
            print("Create an account first")
    elif c==5:
        if account:
            account.check_balance()
        else:
            print("Create an account first")
    elif c==6:
        if isinstance(account,SavingsAccount):
            account.calculate_interest()
        else:
            print("Interest only applicabke for Savings Bank Account")
    elif c==7:
        print("Exiting the bank system.Thank you!!!")
        break
    else:
        print("Invalid choice.Please try again.")



    








