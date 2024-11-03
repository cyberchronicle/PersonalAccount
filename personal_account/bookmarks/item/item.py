class Item:
    def __init__(self, name, discription):
        self.name = name
        self.description = discription

    def __str__(self):
        return f"Item Name: {self.name}, Description: {self.description}"
