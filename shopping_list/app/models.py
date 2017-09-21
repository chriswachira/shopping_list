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

        self.attribs = {"username": self.username,
                   "pwd": self.password,
                   "email": self.email,
                   "date_joined": self.date_joined,
                   "shopping_lists": len(self.shopping_lists)
                  }


        #print(attribs)

        #self._shop = Shop()
        #self._shop.add_user(attribs, self.username)


    def get_attribs(self):
        return {'username': self.username,
                'email': self.email,
                'date_joined': self.date_joined,
                'shopping_lists': len(self.shopping_lists)}






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

users = []
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
        else:
            users.append(attribs)

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
