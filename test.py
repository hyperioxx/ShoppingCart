from ShoppingCart import ShoppingCart
from utils.items import * 
from utils.errors import *

def test_add():
    cart = ShoppingCart()
    item = Apple()
    cart.add(item)
    if len(cart._cart[item.name]) > 1:
        raise Exception("Items in cart should be 1, not {}".format(len(cart._cart[item.name])))


def test_remove():
    cart = ShoppingCart()
    item = Apple()
    cart.add(item)
    cart.add(item)
    cart.remove('apple')
    if len(cart._cart[item.name]) > 1:
        raise Exception("Items in cart should be 1, not {}".format(len(cart._cart[item.name])))


def test_clear():
    cart = ShoppingCart()
    item = Apple()
    cart.add(item)
    cart.add(item)
    cart.clear()
    if cart._cart.get(item.name):
        raise Exception("Items in cart should be 0, not {}".format(len(cart._cart[item.name])))
   


def test_total():
    cart = ShoppingCart()
    item1 = Apple()
    item2 = Banana()
    cart.add(item1)
    cart.add(item1)
    cart.add(item2)
    cart.totals()
    if cart._item_totals['BANANA'] != 2 or cart._item_totals['APPLE'] != 2 or cart._item_totals['TOTAL'] != 4:
        raise Exception("total is incorrect")



def test_discount():
    cart = ShoppingCart()
    item1 = Apple()
    item2 = Banana()
    cart.add(item1)
    cart.add(item1)
    cart.add(item2)
    cart.apply_discount_code("M3GABUCKS")
    if cart._item_totals['TOTAL'] != 2.8:
        raise Exception("total is incorrect")


def test_discount_repeat():
    cart = ShoppingCart()
    item1 = Apple()
    item2 = Banana()
    cart.add(item1)
    cart.add(item1)
    cart.add(item2)
    cart.apply_discount_code("M3GABUCKS")
    try:
        cart.apply_discount_code("M3GABUCKS")
        raise Exception("Failed due to discount code being accepted twice")
    except DiscountCodeAlreadyInUse:
        pass















    





    






