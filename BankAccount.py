#Create a python class called BankAccount with attributes like account_number, balance, date_of_opening and customer_name, and methods like deposit, withdraw, check_balance and customer_details  
#i. The deposit method should return the amount deposited  
#ii. The withdraw method return insufficient balance if account balance is less than amount to be withdrawn else it should return the amount that has been withdrawn.  
#iii. The check_balance method should print the current balance.  
#iv. The customer_details method should print customer name, account number, date of account opening and balance.

class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.balance = 0.0  
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount_deposit): 
        if amount_deposit > 0:
            self.balance += amount_deposit
            return amount_deposit  
        else:
            raise ValueError("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount_withdraw):
        if amount_withdraw <= 0:
            raise ValueError("Invalid withdrawal amount. Please enter a positive value.")
        
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            return amount_withdraw 
        else:
            return "Insufficient balance."

    def check_balance(self):
        print(f"Current balance: {self.balance:.2f}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance:.2f}")

# Example 
account = BankAccount("938476217", "Mercy", "2025-01-20")

# Deposit money into the account
deposited_amount = account.deposit(5000)
print(f"Deposited Amount: {deposited_amount}")

# Check balance after deposit
account.check_balance()

# Withdraw money from the account
withdrawn_amount = account.withdraw(2000)
print(f"Withdrawn Amount: {withdrawn_amount}")

# Check balance after withdrawal
account.check_balance()

# Display customer details
account.customer_details()
