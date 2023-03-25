import pickle
from small_town_teller import Bank, Account, Person


class PersistenceUtils:
    @staticmethod
    def write_pickle(data):
        pickle.dump(data, open('data.pickle', 'wb'))

        # with open('data.pickle', 'wb') as file:
        #   pickle.dump(data, file)

    @staticmethod
    def load_pickle():
        return pickle.load(open('data.pickle', 'rb'))
    # with open('data.pickle', 'rb') as file:
    #   data.update(pickle.load(file))


class Bank(Bank):
    def save_data(self):
        PersistenceUtils.write_pickle(self.accounts)

    def load_data(self):
        self.accounts = PersistenceUtils.load_pickle()
        for value in self.accounts:
            self.add_customer(self.accounts.get(value).ac_owner)


if __name__ == '__main__':
    zc_bank = Bank()
    zc_bank.customers
    # {}
    zc_bank.accounts
    # {}
    zc_bank.save_data()
    zc_bank.load_data()
    print(zc_bank.customers)
    # {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
    print(zc_bank.accounts)
    # {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}
