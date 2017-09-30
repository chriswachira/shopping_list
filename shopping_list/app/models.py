import datetime
import json
from decimal import Decimal

users = [] #The global list of all users registered in the app
items = []

class Item(object):
    """Creates an item"""
    def __init__(self, name, price, descr, *args):
        self.name = name #name of item
        self.price = price #price of item
        self.vendor = args.get("vendor") #item vendor/seller
        #self.quantity = quantity #remaining quantity of item
        #self.descr = descr # item description
        self.rating = 0.0 # average rating of item

    def view_item(self):
        return {"name": self.name,
                "price": self.price,
                "vendor": self.vendor,
                "quantity": self.quantity,
                "descr": self.descr,
                "rating": self.rating
                }

    #def rate_item(self, user_rating):
    #    if user_rating > 5 and user_rating < 0:
    #        return "Rating goes between 0 to 5"
    #    else:

    #        self.rating += user_rating

class ShoppingList(object):
    """Creates Shopping List object"""
    def __init__(self, name, username):
        self.name = name # name of shopping list
        self.author = username # owner of the list by user_id
        self.items = [] # item list in the list
        self.total = 0.0 # float for the total amount of the list's items
        self.likes = [] # list of users who like a shopping list. Program will use the count of
                        # users in the like list to determine total likes

    def add_items(self, name, price, quantity):
        """Adds items to the shopping list"""
        _item = [{name : price}, quantity]
        self.items.append(_item)

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

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

        self.username = email.split('@')[0]
        self.password = password


        #self.date_joined = datetime.datetime.now()
        #self.shopping_lists = []

        self.attribs = {"firstname": self.firstname,
                        "lastname": self.lastname,
                        "username": self.username,
                        "pwd": self.password,
                        "email": self.email}


        #print(attribs)

        #self._shop = Shop()
        #self._shop.add_user(attribs, self.username)


    def get_attribs(self):
        return {'firstname': self.firstname,
                'lastname': self.lastname,
                'username': self.username,
                'email': self.email}






#class Shop(object):
#    def __init__(self):
#        self._users = []
#        #self._filename = "users.json"
#
#    def add_user(self, attribs, username):
        #username = attribs["username"]

        #import os
        #if os.path.isfile(self._filename):
        #    #print(os.getcwd())
        #    with open(self._filename) as usr_obj:
        #        self._attribs = json.dumps(usr_obj)
        #        usernames = []
        #        for attrib in self._attribs:
        #            usernames.append(attrib[0])
        #            if username in usernames:
        #                return "Username already taken"
        #            else:
        #                self._attribs.append(attribs)
        #                with open(self._filename, 'w') as usr_wr:
        #                    json.dumps(self._attribs, usr_wr)

        # else:
        #     with open(self._filename, 'w') as usr_obj:
        #         json.dumps(self._attribs, usr_obj)

        #if len(self._users) == 0:
        #    self._users.append(attribs)
        #    print(self._users)
        #else:
        #    usernames = []
        #    for usr_attribs in self._users:
        #        usernames.append(usr_attribs["username"])
        #        #print("USERS ATTRIBS " + usr_attribs["username"])
        #        if username in usernames:
        #            return "Username already taken! Try another..."
        #        else:
        #            self._users.append(attribs)

        #print(self._users)

    #def remove_user(self, username, password):
    #    with open(self.filename) as usr_obj:
    #        self.users = json.load(usr_obj)
    #        pwd = self.users[username]
    #        if password == pwd:
    #            self.users.pop(username, None)
    #            with open(self.filename, 'w') as usr_obj:
    #                json.dump(self.users, usr_obj, indent=2)
    #                return self.users
    #        else:
    #            return "Password incorrect. Remove user failed."


def add_user(attribs):
    global users
    username = attribs["username"]

    if len(users) == 0:
                users.append(attribs)
                print(users)
    else:
        usernames = []
        for usr_attribs in users:
            usernames.append(usr_attribs["username"])
        if username in usernames:
            return "Username already taken! Try another..."
            print(users)
        else:
            users.append(attribs)
            print(users)

def get_user(username):
        for user in users:
            #print(user)
            if user["username"] == username:
                return user


#def remove_user(username, password):
#    global users
#
#    def search_user(username):
#        for user in users:
#            print(user)
#            if user["username"] == username:
#                return user
#            else:
#                return None
#
#    _user = search_user("bethuel")
#    print(_user)
#    if _user == None:
#        return "User not found."
#    else:
#        password_confirm = _user.get("pwd")
#
#    def find(lst, key, value):
#        for i, dic in enumerate(lst):
#            if dic[key] == value:
#                return i
#        return -1
#
#    if password == password_confirm:
#        user_dict_index = find(users, "username", username)
#        users.pop(user_dict_index)
#    else:
#        return "Password incorrect. Remove user failed."

#make_shopping_list(name, username):
 #   shop_list = ShoppingList(name, username)

