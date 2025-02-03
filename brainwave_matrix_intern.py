import getpass

class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.user_data = {"1234": {"pin": "0000", "balance": 5000}}

    def authenticate(self, card_number):
        if card_number in self.user_data:
            for attempt in range(3):
                pin = getpass.getpass("Enter PIN: ")
                if pin == self.user_data[card_number]['pin']:
                    print("Authentication successful!")
                    return card_number
                else:
                    print("Incorrect PIN. Try again.")
            print("Too many incorrect attempts. Exiting.")
        else:
            print("Card number not recognized.")
        return None

    def check_balance(self, card_number):
        print(f"Your balance is: ${self.user_data[card_number]['balance']}")

    def deposit(self, card_number):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.user_data[card_number]['balance'] += amount
            print(f"${amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, card_number):
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= self.user_data[card_number]['balance']:
            self.user_data[card_number]['balance'] -= amount
            print(f"${amount} withdrawn successfully!")
        else:
            print("Invalid or insufficient funds.")

    def run(self):
        card_number = input("Enter card number: ")
        user = self.authenticate(card_number)
        if user:
            while True:
                print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
                choice = input("Choose an option: ")
                if choice == '1':
                    self.check_balance(user)
                elif choice == '2':
                    self.deposit(user)
                elif choice == '3':
                    self.withdraw(user)
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
