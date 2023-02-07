from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to access all attributes and methods
        super().__init__(name, price, quantity)

        # Run validations to the received arguments
        assert broken_phones >= 0, f"{broken_phones} is not greater than or equal to zero"

        # Assign to self object
        self.__broken_phones = broken_phones

    @property
    def broken_phones(self):
        return self.__broken_phones

    @broken_phones.setter
    def broken_phones(self, value):
        self.__broken_phones = value
