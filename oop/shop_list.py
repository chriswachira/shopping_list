class ShoppingList(object):
    """Creates Shopping List object"""
    def __init__(self, name, user_id):
        self.name = name # name of shopping list
        self.owner = user_id # owner of the list by user_id
        self.items = [] # item list in the list
        self.total = 0.0 # float for the total amount of the list's items
        self.likes = [] # list of users who like a shopping list. Program will use the count of
                        # users in the like list to determine total likes

    def add_items(self, item_id):
        """Adds items to the shopping list"""
        self.items.append(item_id)

    def remove_item(self, item_id):
        """Removes items from the list"""
        self.items.pop(item_id)

    def checkout(self):
        """Returns the total price of the shopping list's items"""
        for item in self.items:
            self.total = self.total + item.price

        print("Total: " + self.total)
        return self.total

    def like(self, user_id):
        """Adds likes to a shopping list"""
        self.likes.append(user_id)

