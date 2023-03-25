import pickle


class Person:
    def __init__(self, identification, first_name, last_name):
        self.id = identification
        self.firstname = first_name
        self.lastname = last_name


class Account:
    def __init__(self, ac_number, ac_type, ac_owner):
        self.number = ac_number
        self.type = ac_type
        self.owner = ac_owner
        self.balance = 0


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_customer(self, person: Person):
        if person.id in self.customers:
            print("You are current customer!")
        else:
            full_name = person.firstname + " " + person.lastname
            self.customers[person.id] = full_name
            print(f"Thank you {full_name}. Your name has been added to customer list\n")

    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            print("Please add customer into customer list first")
        elif account.number in self.accounts:
            print(f"Account {account.number} already exist")
        else:
            self.accounts[account.number] = account

    def delete_account(self, identification, ac_number):
        if identification not in self.customers:
            print("Customer is not in customer list")
        elif ac_number not in self.accounts:
            print("Account is not exist to remove")
        else:
            del self.accounts[ac_number]

    def deposit(self, ac_number, deposit_amount):
        if ac_number not in self.accounts:
            print("Account not exist")
        elif deposit_amount <=0:
            print("Deposit amount is not valid")
        else:
            deposit_account = self.accounts.get(ac_number)
            deposit_account.balance += deposit_amount
            print(f"{deposit_amount} has been deposited into your account\n"
                  f"Current balance is {deposit_account.balance}\n")

    def withdrawal(self, ac_number, withdraw_amount):
        if ac_number in self.accounts:
            withdraw_account = self.accounts.get(ac_number)
            if withdraw_account.balance < withdraw_amount:
                print("You don't have enough money")
            else:
                withdraw_account.balance -= withdraw_amount
                print(f"{withdraw_amount} has been withdrawn from your account.\n"
                      f"Current balance is {withdraw_account.balance}\n")


    def balance_inquiry(self, ac_number):
        if ac_number in self.accounts:
            ac_balance = self.accounts.get(ac_number).balance
            print(f'Thanks for checking. Your account balance is {ac_balance}\n')
            return ac_balance
        else:
            print('Account is not exist')


if __name__ == "__main__":
    zc_bank = Bank()
    bob = Person(1, "Bob", "Smith")
    zc_bank.add_customer(bob)
    bob_savings = Account(1001, "SAVINGS", bob)
    zc_bank.add_account(bob_savings)
    zc_bank.balance_inquiry(1001)
    # 0
    zc_bank.deposit(1001, 256.02)
    zc_bank.balance_inquiry(1001)
    # 256.02
    zc_bank.withdrawal(1001, 128)
    zc_bank.balance_inquiry(1001)
    # 128.02


