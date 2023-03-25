# Part 10

## Accompanying resources
* Slide deck: https://zipcoder.github.io/reveal-slides.data-engineering/zcw_content/python/fundamentals-part10.html

## Exercise 1

Create a program called *small_town_teller.py*

Declare a **Person** class with the following attributes:
* id
* first name
* last name

Declare an **Account** class with the following attributes:
* number
* type
* owner
* balance

Declare a **Bank** class able to support the following operations:
* Adding a customer to the bank
* Adding an account to the bank
* Removing an account from the bank
* Depositing money into an account
* Withdrawing money from an account
* Balance inquiry for a particular account

From an interactive terminal, you should be able to import these classes an interact with the objects and methods defined above.

**Constraints**

* When attempting to register a customer, the customer id must be unique.
* When attempting to add an account, the user associated with said account must already registered as a customer.
* When attempting to add an account, the account number must be unique.


```python
from small_town_teller import Person, Account, Bank

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
```

## Exercise 2 

Create a program called *persistent_small_town_teller.py*

Declare a **PersistenceUtils** class with the following static methods:
* write_pickle
* load_pickle

Append the following methods to the **Bank** class:
* save_data
* load_data

This application should extend exercise one so that all of the customers and accounts persist between restarts.

From an interactive terminal:
* Create customers and accounts. 
* Save the data using the save_data method.
* Exit the session.
* Create a new session.
* Validate there are no customers and no accounts.
* Load the saved data using the load_data method.
* Validate the persistence is working.

```python
from persistent_small_town_teller import Person, Account, Bank1

zc_bank = Bank1()
zc_bank.customers
# {}
zc_bank.accounts
# {}
zc_bank.load_data()
zc_bank.customers
# {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
zc_bank.accounts
# {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}
```