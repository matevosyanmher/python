import csv


class Item:
    __all_items = []
    __discount = 0.0
    _object_count = 0

    def __init__(self, name: str, price: float, quantity: int):
        """assertions"""
        try:
            assert isinstance(name, str), "Name must be a string"
            assert isinstance(price, float), "Price must be a float"
            assert isinstance(quantity, int), "Quantity must be an integer"
            assert quantity > 0, "Quantity must be greater than 0"
            assert price > 0, "Price must be greater than 0"
            assert name not in self.__all_items, "Item already exists"
        except AssertionError as error:
            print(error)
            # exit()

        self.name = name
        self.price = price
        self.quantity = quantity
        Item._object_count += 1

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.quantity}"

    def add_price_by(self, percentage: float):
        assert 0 <= percentage <= 100, "Percentage must be between 0 and 100"
        self.price += self.price * percentage / 100
        return self.price

    def calculate_total_price(self):
        assert 0 <= self.discount <= 100, "Discount must be between 0 and 100"
        if self.discount > 0:
            return round(self.price * self.quantity * (1 - self.discount / 100), 2)
        else:
            return self.price * self.quantity

    # read the csv file and create a list of items
    @classmethod
    def read_csv_file(cls, file_name):
        with open(file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name, price, quantity = row
                cls.__all_items.append(Item(name, float(price), int(quantity)))

    @classmethod
    def get_all_items(cls):
        return cls.__all_items

    @classmethod
    def get_discount(cls):
        return cls.__discount

    @classmethod
    def set_discount(cls, __discount):
        cls.discount = __discount

    # get object count
    @classmethod
    def get_object_count(cls):
        return cls._object_count


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, brand: str):
        super().__init__(name, price, quantity)
        self.brand = brand

    # setter of discount
    def set_discount(self, discount):
        super().set_discount(discount)

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.quantity} - {self.brand}"


Item.read_csv_file('ObjectName.csv')
print(Item.get_all_items())
print(Item.get_object_count())
