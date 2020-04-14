
class _ItemBase:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Apple(_ItemBase):
    def __init__(self, price=1):
        super().__init__("APPLE", price)


class Banana(_ItemBase):
    def __init__(self, price=2):
        super().__init__("BANANA", price)


class Orange(_ItemBase):
    def __init__(self, price=3):
        super().__init__("ORANGE", price)






    

    