import csv


class Item:
    """

    """
    pay_rate = 0.8  # the amount to be paid after 20% discount.
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        """
        constructing the class Item for instantiating
        :param name:
        :param price:
        :param quantity:
        """

        # Run validations to the received arguments
        assert price >= 0, f"{price} is not greater than or equal to zero"
        assert quantity >= 0, f"{quantity} is not greater than or equal to zero"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def calculate_total_price(self):
        return self.__price * self.__quantity

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(f'{filename}', 'r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # ignore .0 floats
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.__price}', '{self.__quantity}')"
