class ShoppingCart:
    """A simple shopping cart implementation.

    This implementation supports both the basic example from the slides
    and the more advanced features with quantity.
    """

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
        self._discount = 0

    def add_item(self, name, price):
        """Add an item to the cart.

        Args:
            name (str): The name of the item
            price (float): The price per unit
        """
        self.items[name] = price

    def remove_item(self, name):
        """Remove an item from the cart.

        Args:
            name (str): The name of the item to remove
        """
        if name in self.items:
            del self.items[name]

    def apply_discount(self, percentage):
        """Apply a percentage discount to the cart.

        Args:
            percentage (float): The percentage discount to apply
        """
        self._discount = percentage / 100

    def total(self):
        """Calculate the total price of all items in the cart.

        Returns:
            float: The total price
        """
        subtotal = sum(self.items.values())

        # Apply discount
        return subtotal * (1 - self._discount)
