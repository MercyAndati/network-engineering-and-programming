class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening):
        self.account_number = account_number
        self.balance = 0.0  # Initial balance is set to 0
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount_deposit):
        """Deposit a specified amount into the account."""
        if amount_deposit > 0:
            self.balance += amount_deposit
            return amount_deposit  # Return the amount deposited
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount_withdraw):
        """Withdraw a specified amount from the account."""
        if amount_withdraw <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if self.balance >= amount_withdraw:
            self.balance -= amount_withdraw
            return amount_withdraw  # Return the amount withdrawn
        else:
            return "Insufficient balance."

    def check_balance(self):
        """Print the current balance."""
        print(f"Current balance: {self.balance:.2f}")

    def customer_details(self):
        """Print the customer's details."""
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance:.2f}")

# Example usage:
account = BankAccount("123456789", "Mercy", "2025-01-20")

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
