# Program for keeping an account of
# withdrawal and deposits in a bank using OOP
class bank:

    # Instance Attribute : name of owner and current balance
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # magic_method: string
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    # Instance Method : making a deposit
    def deposit(self, depo):
        self.balance = self.balance + depo
        print("Deposit of $" + str(depo) + " Accepted")

    # Instance Method : making a withdrawal
    def withrdrawal(self, withdraw):
        self.balance = self.balance - withdraw
        if self.balance >= 0:
            print("Withdrawal of $" + str(withdraw) + " Accepted")
        else:
            print("Insufficient Funds for withdrawal")


# driver program
acct1 = bank("Jose", 100)
print(acct1)

print(acct1.owner)
print(acct1.balance)

acct1.deposit(50)
acct1.withrdrawal(100)
acct1.withrdrawal(150)
