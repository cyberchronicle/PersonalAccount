from ..item import item


class Shelf:
    def __init__(self, name):
        self.name: str = name
        self.items: list[item.Item] = []

    def change(self, new_name):
        self.name: str = new_name

    def add_item(self, new_bookmark):
        if isinstance(new_bookmark, item.Item):
            self.items.append(new_bookmark)
        else:
            raise ValueError("Only Bookmark instances can be added to the shelf.")

    def show(self):
        if not self.items:
            return "The shelf is empty."
        return f"Shelf '{self.name}' contains:\n" + "\n".join(str(bookmark)
                                                              for bookmark in self.items)
