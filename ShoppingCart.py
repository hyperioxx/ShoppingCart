from utils.items import _ItemBase
from utils.errors import ItemNotValid, InvalidDiscountCode, DiscountCodeAlreadyInUse

class ShoppingCart:

    def __init__(self):
        """
        Shopping Cart Constructor
        """
        self._cart = {} # "private" variable _cart
        self._item_totals = {"Total" : 0 }
        self._valid_distcount_code = {"FREEMONEY" : 10, "D1SC0UNT": 20, "M3GABUCKS": 30}
        self._discountcode_history = [] # "private" variable _discountcode_history
        self._discount_total = 

    def add(self, item):
        """gives the ability of adding items to an instance of ShoppingCart
        
        :param item: is a dict containing items name and price
        :type item: ItemBase
        """
        if not isinstance(item, _ItemBase):
            raise ItemNotValid()

        if not self._cart.get(item.name):
            self._cart[item.name] = [item]
            self._item_totals[item.name] = item.price    
            return

        self._cart[item.name].append(item)
        self._item_totals[item.name] += item.price 
        

    def remove(self, itemkey):
        """gives the ability to remove items from an instance of ShoppingCart
        
        :param itemkey: name of the item you want to remove
        :type itemkey: str
        """
        itemkey = itemkey.upper()
        ref = self._cart[itemkey][0]
        self._item_totals[itemkey] -= ref.price
        self._cart[itemkey].pop()


    def clear(self):
        """
        Removes all items, totals and discount codes 
        """
        self._cart = {} 
        self._item_totals = {}
        self._discountcode_history = {}


    def totals(self):
        """Prints agragated totals
        """
        for key, value in self._item_totals.items():
            print("{}\t£{}".format(key.title(), value))


    def apply_discount_code(self, discountcode):
        """Give user the ability to apply a discount code to shopping cart
        
        :param discountcode: discount code as string
        :type discountcode: str
        """
        if discountcode not in self._valid_distcount_code:
            raise InvalidDiscountCode()

        if discountcode in self._discountcode_history:
            raise DiscountCodeAlreadyInUse()









        



            
        




    
        

    

    
