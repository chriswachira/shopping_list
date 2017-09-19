class Item(object):
    def __init__(self, item_name, price, vendor, quantity, descr, rating):
        self.name = item_name
        self.price = price
        self.vendor = vendor
        self.quantity = quantity
        self.descr = descr
        self.rating = rating

    def get_attribs(self):
        return {"Name": self.name,
                "Price": self.price,
                "Vendor": self.vendor,
                "Quantity": self.quantity,
                "Description": self.descr,
                "Rating": self.rating}

