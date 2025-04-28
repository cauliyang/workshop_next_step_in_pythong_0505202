class ShoppingCart:
    """A simple shopping cart implementation."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}
        self._discount_percentage = 0

    def add_item(self, name, price, quantity=1):
        """Add an item to the cart.

        Args:
            name (str): The name of the item
            price (float): The price per unit
            quantity (int, optional): The quantity to add. Defaults to 1.
        """
        if name in self.items:
            # Update existing item quantity
            self.items[name]["quantity"] += quantity
        else:
            # Add new item
            self.items[name] = {"price": price, "quantity": quantity}

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
        self._discount_percentage = percentage

    def total(self):
        """Calculate the total price of all items in the cart.

        Returns:
            float: The total price
        """
        subtotal = sum(item["price"] * item["quantity"] for item in self.items.values())

        if self._discount_percentage > 0:
            discount = subtotal * (self._discount_percentage / 100)
            return subtotal - discount

        return subtotal
