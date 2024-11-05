from shelf import shelf


# initialisation of shelves, so exists at least one shelf, and it can't be removed
shelves: list[shelf.Shelf] = [shelf.Shelf("Didn't sorted yet")]
