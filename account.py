class Account:
    """
  This is a class that represents someone's account.
    """
    def __init__(self, name) -> None:
        """
        This creates the Account object that includes a name and a account balance of 0.
        :name: The account name
        :balance: the default balance of the account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount) -> bool:
        """
        Deposits the amount that is entered.
        :amount: The deposit amount.
        :bool: True if the deposit goes through, and false if it does not.
        """
      
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount) -> bool:
        """
        Withdraws the amount that is chosen.
        :amount: Withdraw amount.
        :bool: True if the withdraw transaction goes through, false if it does not.
        """
        if amount > 0 and amount <= self.__balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Gets the current account balance.
        :balance: The Current balance of the account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Gets the name of the account.
        :name: The name of the account.
        """
        return self.__account_name


