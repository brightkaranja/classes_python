rom datetime import datetime
class Transaction:
    def __init__(self, narration, amount, transaction_type):
        self.date_time = datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type = transaction_type
    def __str__(self):
        return f"{self.date_time}: {self.transaction_type} of {self.amount}. Narration: {self.narration}"
        
class Account:
    def __init__(self, name, balance=0):
        self.__account_number = account_number
        self.__name = name
        self.__balance = 0
        self.__deposits = []
        self.withdrawals = []
        self.transactions = []
        self.__loan_balance = 0
        self.__loan_history = []
        self.__is_frozen=False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append(f"Deposited: {amount}, New balance: {self.balance}")
            print(f"Deposited: {amount}, New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.withdrawals.append(f"Withdrawn: {amount}, New balance: {self.__balance}")
            print(f"Withdrawn: {amount}, New balance: {self.__balance}")
        else:
            print("You have insufficient funds or invalid amount.")

    def show_balance(self):
        print(f"Current balance: {self.__balance}")

    def transfer_funds(self, amount, recipient):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            recipient.deposit(amount)
            transfer_account.deposit(amount)
        transaction = Transaction(f"Transfer to {recipient.get_owner_name()}", amount, "transfer")
        self.transactions.append(transaction)
        return f"Hello {self.__name} your transfer was successful. New balance: {self.get_balance()}"
            
    def request_loan(self, amount):
        loan_limit=3000
        if amount<0:
            return "Loan must be positive"
        if amount>loan_limit:
            return f"Hello {self.__name} loan amount has exceeded the limit of {loan_limit}"
        if self.__loan_amount>0:
            return f"Hello {self.__name} you have an oustanding loan to be paid"
        self.__loan_amount +=amount
        self.__balance += amount
        transaction = Transaction(f"Loan requested", amount, "request loan")
        self.transactions.append(transaction)
        return f"Hello {self.__name} loan request for {amount} has been approved. New balance: {self.get_balance()}"

    def repay_loan(self, amount):
        if amount <= self.loan_balance and amount > 0 :
          self.__loan_balance -= amount
          self.__balance -= amount
          self.loan_history.append(f"Loan repaid: {amount}, Remaining loan: {self.__loan_balance}")
          print(f"Loan repaid: {amount}, Remaining loan: {self.__loan_balance}, Current balance: {self.__balance}")
        elif amount > self.__loan_balance:
            print(f"Amount exceeds outstanding loan. Remaining loan {self.__loan_balance}")
        else:
          print("Invalid amount.")

    def view_account_details(self):
        return f"Account Owner: {self.__owner}, Current Balance: {self.balance}, Loan Amount: {self.loan_amount}"

    def change_account_owner(self, new_owner):
        self.__owner = new_owner
        return f"Account owner changed to {self.owner}"

    def get_statement(self):
        print("Statement:")
        for transaction in self.deposits + self.withdrawals:
            print(transaction)
            
    def get_loan_statement(self):
      print("Loan Statement:")
      for record in self.loan_history:
        print(record)

    def interest_calculation(self):
        interest = self.__balance * 0.05
        self.__balance += interest
        self.transactions.append(transaction)
        return f"Interest of {interest} applied. New balance: {self.balance}"

    def freeze_account(self):
        self.is_frozen = True
        return "Account has been frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account has been unfrozen."

    def set_minimum_balance(self, amount):
        if amount < 0:
            return "Minimum balance cannot be negative."
        self.__minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}"

    def close_account(self):
        self.balance = 0
        self.loan_amount = 0
        self.transactions.clear()
        return "Account closed. All balances set to zero and transactions cleared."


    def get_owner_name(self):
        return self.__owner_name