import pytest

from foo.supermarket import *

def test_cart_empty():
    cart = Cart()
    assert cart.total() == 0

