

class ItemNotValid(Exception):
    def __init__(self):
        super().__init__("The Item you have to add is and invalid item")


class InvalidDiscountCode(Exception):
    def __init__(self):
        super().__init__("The discount code you have supplied is invalid")

class DiscountCodeAlreadyInUse(Exception):
    def __init__(self):
        super().__init__("The discount code you have supplied has aleady been applied")