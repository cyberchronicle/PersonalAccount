from datetime import datetime


# Item is a wrap for bookmark (for storing and sorting)
class Item:
    def __init__(self, name, new_id, added_at):
        self.name: str = name
        self.id: int = new_id
        self.added_at: datetime = added_at

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> int:
        return self.id

    def get_added_at(self) -> datetime:
        return self.added_at

    def get_text(self):
        # TODO: make call to database to get text from id
        print(self.name)

    def __str__(self):
        return f"Item Name: {self.name}, Id: {self.id}"
