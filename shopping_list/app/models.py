import datetime
import json
from decimal import Decimal

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

class User(object):
    """Creates User's object"""

    def __init__(self, email, password):
        self.email = email

        self.username = email.split('@')[0]
        self.password = password

        self.date_joined = datetime.datetime.now()
        self.shopping_lists = []

    def get_attribs(self):
        return {'username': self.username,
                'email': self.email,
                'date_joined': self.date_joined,
                'shopping_lists': len(self.shopping_lists)}




class Shop(object):
    def __init__(self):
        self.users = {}
        self.filename = "users.json"

    def add_user(self, username, password):

        import os
        if os.path.isfile(self.filename):
            #print(os.getcwd())
            with open(self.filename) as usr_obj:
                self.users = json.load(usr_obj)
                if username in self.users.keys():
                    return "Username already taken"
                else:
                    self.users[username] = password
                    with open(self.filename, 'w') as usr_wr:
                        json.dump(self.users, usr_wr, indent=2)

        else:
            with open(self.filename, 'w') as usr_obj:
                json.dump(self.users, usr_obj, indent=2)


        print(self.users)

    def remove_user(self, username, password):
        with open(self.filename) as usr_obj:
            self.users = json.load(usr_obj)
            pwd = self.users[username]
            if password == pwd:
                self.users.pop(username, None)
                with open(self.filename, 'w') as usr_obj:
                    json.dump(self.users, usr_obj, indent=2)
                    return self.users
            else:
                return "Password incorrect. Remove user failed."



