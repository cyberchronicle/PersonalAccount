from app import bookmarks
from shelf import shelf


def get_shelfs() -> list[shelf.Shelf]:
    return bookmarks.shelves


def add_shelf(name: str):
    if name not in bookmarks.shelves:
        bookmarks.shelves.append(shelf.Shelf(name=name))
    else:
        raise Exception(f"Shelf '{name}' already exists")


def remove_shelf(name: str):
    if name != "Didn't sorted yet":
        bookmarks.shelves.remove(shelf.Shelf(name=name))
    else:
        raise Exception("This shelf cannot be removed")


def get_shelf(index: int) -> shelf.Shelf:
    if index < len(bookmarks.shelves):
        return bookmarks.shelves[index]
    raise Exception("Shelf index out of range")
