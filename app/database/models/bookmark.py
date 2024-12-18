from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.models import Base


class Shelf(Base):
    __tablename__ = 'shelf'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_user = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String)


class Bookmark(Base):
    __tablename__ = 'bookmarks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)


class BookmarkInShelf(Base):
    __tablename__ = 'bookmarks_inshelf'
    fk_shelf = Column(Integer, ForeignKey('shelf.id', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True, nullable=False)
    fk_bookmark = Column(Integer, ForeignKey('bookmarks.id', onupdate='CASCADE', ondelete='CASCADE'),
                         primary_key=True, nullable=False)
