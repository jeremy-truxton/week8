#Made a SuperClass called BankAccount
class BankAccount:

    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance

    def withdrawl(self, withdrawn):
        if float(withdrawn) > self.balance:
            return "You do not have a large enough balance to make that withdrawal."
        elif float(withdrawn) <= 0:
            return "That is not a valid amount to withdraw."
        else:
            self.balance -= float(withdrawn)
            return "You have withdrawn " + str(withdrawn) + "$, your new balance is " + str(self.balance) + "$."

    def deposit(self, amount):
        if float(amount) <= 0:
            return "That is not a valid amount to deposit."
        else:
            self.balance += float(amount)
            return "You have deposited " + str(amount) + "$, your new balance is " + str(self.balance) + "$."

    def getbalance(self):
        return "Your current balance is " + str(self.balance) + "$."

#Made a Sub-class called CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, accountnumber, balance, fees, minimum_balance):
        super().__init__(accountnumber, balance)
        self.fees = fees
        self.minimum_balance = minimum_balance

    def check_minimum_balance(self):
        need = self.minimum_balance - self.balance
        if need > 0:
            return "The minimum balance in your account is " + str(self.minimum_balance) + "$."
        else:
            return "The minimum balance in your account is " + str(self.minimum_balance) + "$."

    def deduct_fees(self):
        if self.balance > self.fees:
            self.balance -= self.fees
            return "Fees were deducted. Your new balance is " + str(self.balance) + "$."
        else:
            return "Not enough money in the account to deduct fees."

#Made a Sub-class called SavingsAccount
class SavingsAccount(BankAccount):
    def __init__(self, accountnumber, balance, interest_rate):
        super().__init__(accountnumber, balance)
        self.interest_rate = interest_rate
    def add_interest_rate(self):
        self.balance += self.balance * (self.interest_rate/100)
        return "Your new balance is " + str(self.balance) + "$."

checking = CheckingAccount(000000, 25, 5, 50)
savings = SavingsAccount(000000, 100, 2)

while True:  # create loop to prompt for checking and savings
    prompt = input("Please input either 'C' for checking account or 'S' for Savings account (input 'E' anytime to exit). ")
    if prompt.lower() == 'c':
        while True:  # create loop for Checking options
            if checking.balance < checking.minimum_balance:
                prompt = input("ALERT: Your account balance is lower than the minimum balance required. Please deposit " + str(checking.minimum_balance - checking.balance) + "$. Input anything to continue (input 'E' anytime to exit). ")
                if prompt.lower() == 'e':
                    exit()
            prompt = input("Please input: \n'1' to make a withdrawal, \n'2' to make a deposit, \n'3' to get your account balance,"
                        " \n'4' to deduct fees, \n'5' to check the minimum balance, \ninput anything else to go back, \ninput 'E' anytime to exit. ")
            if prompt == '1':
                try:
                    prompt = input("Please input an amount of money (in dollars) to withdraw or input anything else to go back (input 'E' anytime to exit). $")
                    print(checking.withdrawl(prompt))
                except ValueError:
                    if prompt.lower() == 'e':
                        exit()
            elif prompt == '2':
                try:
                    prompt = input("Please input an amount of money (in dollars) to deposit or input anything else to go back (input 'E' anytime to exit). $")
                    print(checking.deposit(prompt))
                except ValueError:
                    if prompt.lower() == 'e':
                        exit()
            elif prompt == '3':
                print(checking.getbalance())
            elif prompt == '4':
                print(checking.deduct_fees())
            elif prompt == '5':
                print(checking.check_minimum_balance())
            elif prompt == 'e':
                exit()
            else:
                break
    elif prompt.lower() == 's':
        while True:  # create loop for Savings options
            prompt = input("Please input: \n'1' to make a withdrawal, \n'2' to make a deposit, \n'3' to get your account balance,"
                        " \n'4' to add the interest rate \ninput anything else to go back, \ninput 'E' anytime to exit. ")
            if prompt == '1':
                try:
                    prompt = input("Please input an amount of money (in dollars) to withdraw or input anything else to go back (input 'E' anytime to exit). $")
                    print(savings.withdrawl(prompt))
                except ValueError:
                    if prompt.lower() == 'e':
                        exit()
            elif prompt == '2':
                try:
                    prompt = input("Please input an amount of money (in dollars) to deposit or input anything else to go back (input 'E' anytime to exit). $")
                    print(savings.deposit(prompt))
                except ValueError:
                    if prompt.lower() == 'e':
                        exit()
            elif prompt == '3':
                print(savings.getbalance())
            elif prompt == '4':
                print(savings.add_interest_rate())
            elif prompt == 'e':
                exit()
            else:
                break
    elif prompt.lower() == 'e':
        exit()
    else:
        print("That is not a valid entry!")
        continue
