import pytest

# This is our test file for a shopping cart that hasn't been implemented yet
# We'll follow TDD principles: write tests first, then implement the functionality

def test_cart_creation():
    """Test that a new cart starts empty."""
    cart = ShoppingCart()
    assert len(cart.items) == 0
    assert cart.total() == 0

def test_add_item():
    """Test adding items to the cart."""
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 2)
    assert len(cart.items) == 1
    assert cart.total() == 2.0
    
    cart.add_item("banana", 0.5, 3)
    assert len(cart.items) == 2
    assert cart.total() == 3.5

def test_remove_item():
    """Test removing items from the cart."""
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 2)
    cart.add_item("banana", 0.5, 3)
    
    cart.remove_item("apple")
    assert len(cart.items) == 1
    assert cart.total() == 1.5
    
    # Removing a non-existent item should not cause an error
    cart.remove_item("orange")
    assert len(cart.items) == 1
    assert cart.total() == 1.5

def test_apply_discount():
    """Test applying discounts to the cart."""
    cart = ShoppingCart()
    cart.add_item("apple", 1.0, 2)
    cart.add_item("banana", 0.5, 3)
    
    # 10% discount
    cart.apply_discount(10)
    assert cart.total() == 3.15  # 3.5 * 0.9 = 3.15