class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        self.loan_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append(f"Deposited: {amount}, New balance: {self.balance}")
            print(f"Deposited: {amount}, New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.withdrawals.append(f"Withdrawn: {amount}, New balance: {self.balance}")
            print(f"Withdrawn: {amount}, New balance: {self.balance}")
        else:
            print("You have insufficient funds or invalid amount.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

    def transfer_funds(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient funds or invalid amount for transfer.")

    def request_loan(self, amount):
      if self.loan_balance == 0:
        self.loan_balance = amount
        self.balance += amount
        self.loan_history.append(f"Loan requested: {amount}, Outstanding loan: {self.loan_balance}")
        print(f"Loan taken: {amount}, Outstanding loan: {self.loan_balance}, Current balance: {self.balance}")
      else:
        print("Outstanding loan exists. Repay it first.")

    def repay_loan(self, amount):
        if amount <= self.loan_balance and amount > 0 :
          self.loan_balance -= amount
          self.balance -= amount
          self.loan_history.append(f"Loan repaid: {amount}, Remaining loan: {self.loan_balance}")
          print(f"Loan repaid: {amount}, Remaining loan: {self.loan_balance}, Current balance: {self.balance}")
        elif amount > self.loan_balance:
            print(f"Amount exceeds outstanding loan. Remaining loan {self.loan_balance}")
        else:
          print("Invalid amount.")

    def view_account_details(self):
        return f"Account Owner: {self.owner}, Current Balance: {self.balance}, Loan Amount: {self.loan_amount}"

    def change_account_owner(self, new_owner):
        self.owner = new_owner
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
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest applied: {interest}")
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
        self.minimum_balance = amount
        return f"Minimum balance set to {self.minimum_balance}"

    def close_account(self):
        self.balance = 0
        self.loan_amount = 0
        self.transactions.clear()
        return "Account closed. All balances set to zero and transactions cleared."