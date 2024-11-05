import item


# Shelf stores bookmarks (their names and identificators)
class Shelf:
    def __init__(self, name: str):
        self.name: str = name
        self.items: list[item.Item] = []

    def change_name(self, new_name: str):
        self.name: str = new_name

    def add_item(self, new_bookmark: item.Item):
        if isinstance(new_bookmark, item.Item):
            self.items.append(new_bookmark)
        else:
            raise ValueError("Only Bookmark instances can be added to the shelf.")

    def remove_item(self, index: int):
        if index >= len(self.items):
            print("Index out of range.")
        self.items.pop(index)

    # Not completed function for giving information
    # TODO: choose format and complete the function (add 2 sorting modes with names and added_at)
    def show(self):
        if not self.items:
            return "The shelf is empty."
        return f"Shelf '{self.name}' contains:\n" + "\n".join(str(bookmark)
                                                              for bookmark in self.items)
