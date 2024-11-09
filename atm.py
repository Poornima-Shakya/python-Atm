
# define the ATM class
class ATM:
    
    def __init__(self):
        # Initialize the ATM with the default values
        self.balance = 0.0  # User's account balance
        self.pin = "1234"   # Default PIN for the ATM
        self.transaction_history = []  # List to  store the transaction history

    def display_menu(self):
        # Display the ATM menu options

        print("\n--- ATM Menu ---")
        print("1. Account Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

    def account_balance_inquiry(self):
        # Show the current account balance
        print(f"Your current balance is: ${self.balance:.2f}")

    def cash_withdrawal(self):
        # Allow the user to withdraw the cash
        amount = float(input("Enter the amount to withdraw: $"))
        # Check if there are the sufficient funds
        if amount <= self.balance:
            self.balance -= amount  # Deduct amount from balance
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")  # Log the transaction
            print(f"Please take your cash: ${amount:.2f}")
        else:
            print("Insufficient funds!")  # Notify user of insufficient funds

    def cash_deposit(self):
        # Allow the user to deposit the  cash
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount  # Add amount to balance
        self.transaction_history.append(f"Deposited: ${amount:.2f}")  # Log the transaction
        print(f"Successfully deposited: ${amount:.2f}")

    def change_pin(self):
        # Allow the user to change their PIN
        new_pin = input("Enter your new PIN to change : ")
        self.pin = new_pin  # Update the PIN
        print("your PIN changed successfully.")

    def transaction_history_view(self):
        # Display the user's transaction history
        if not self.transaction_history:
            print("No transaction history available.")  # Notify if no transactions exist
        else:
            print("\n--- Transaction History ---")
            for transaction in self.transaction_history:
                print(transaction)  # Print the each transaction

    def authenticate_user(self):
        # Authenticate the user with PIN
        attempts = 3  # the Number of attempts allowed
        while attempts > 0:
            entered_pin = input("Please enter your PIN: ")
            if entered_pin == self.pin:
                print("PIN accepted.")
                return True  # Authentication is successful
            else:
                attempts -= 1
                print(f"Incorrect PIN. You have {attempts} attempts left.")
        print("Too many incorrect attempts. Exiting.")
        return False  # Authentication is  failed

    def run(self):
        # Main loop to run the ATM program
        if not self.authenticate_user():  # Authenticate the user before proceeding
            return  # Exit if authentication fail

        while True:
            self.display_menu()  # Show the menu
            choice = input("Select an option between (1-6): ")  # Get the user choice
            if choice == '1':
                self.account_balance_inquiry()  # show the account balance inquiry
            elif choice == '2':
                self.cash_withdrawal()  # show the  Cash withdrawal
            elif choice == '3':
                self.cash_deposit()  # show the Cash deposit
            elif choice == '4':
                self.change_pin()  # Change the PIN
            elif choice == '5':
                self.transaction_history_view()  # View the transaction history
            elif choice == '6':
                print("Thank you for using the ATM. Goodbye!")  # Exit the  message
                break  # Exit the loop
            else:
                print("Invalid option. Please try again.")  # invalid input

# Entry point of the program to start
if __name__ == "__main__":
    atm = ATM()  # Create an instance of the ATM
    atm.run()  # Start the ATM program