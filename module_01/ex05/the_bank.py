class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str) :
            raise AttributeError("Attribute name must be a str object.")

    def __str__(self) :
        return str([[f"{attribute} = {getattr(self, attribute)}"] for attribute in dir(self) if not attribute.startswith('__')])

class Bank(object) :
    """The bank"""
    def __init__(self):
        self.accounts = []
    def __str__(self) :
       return '\n'.join(str(account) for account in bank.accounts)

    def check_if_corrupted(self, account) :
        if not isinstance(account, Account) :
            raise ValueError("account must be an Account object.")

        attr = [attribute for attribute in dir(account) if not attribute.startswith('__')]
        print(len(attr))
        if len(attr) % 2 == 0 or any(attribute.startswith(('b', 'zip', 'addr')) for attribute in attr) :
            print("lo")
            return True
        if not all(hasattr(account, attr) for attr in ["name", "id", "value"]):
            print("lolo")
            return True
        if not isinstance(account.name, str) or not isinstance(account.id, int) or not isinstance(account.value, (int, float)) :
            print("lolo3")
            return True
        return False

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return True if success, False if an error occured
        """
        if not isinstance(new_account, Account) :
            return False
        if self.check_if_corrupted(new_account) or any(new_account.name == a.name for a in self.accounts) :
            print("error adding")
            return False

        self.accounts.append(new_account)
        return True

    def transfer(self, origin: str, dest: str, amount: int):
        """" Perform the fund transfer
            @origin: str(name) of the first account
            @dest:  str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        if not isinstance(origin, str) or not isinstance(dest, str) or not isinstance(amount, (int, float)) :
            return False
        originAccount = next((account for account in self.accounts if getattr(account, "name") == origin), None)
        destAccount = next((account for account in self.accounts if getattr(account, "name") == dest), None)
        if self.check_if_corrupted(originAccount) and self.check_if_corrupted(destAccount) :
            return False
        if amount < 0 or originAccount.value < amount :
            return False
        if (originAccount == destAccount) :
            return True


    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:  str(name) of the account
            @return True if success, False if an error occured
        """
        # ... Your code ...

    def transfer(self, amount):
        self.value += amount

if __name__ == "__main__" :
    bank = Bank()
    dict = {'arg1': 1, 'arg2': 2, 'arg3': 3}
    cuenta = Account("nombre", **dict)
    #setattr(cuenta, "atr1", True)

    print(bank.add(cuenta))

    print(bank)
   # print(''.join(str(account) for account in bank.accounts))

    cuenta.name = "otro"
    cuenta2 = Account("nombre", **dict)

    print(bank.add(cuenta2))
    print(bank)

