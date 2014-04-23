import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SQLAlchemy_Example import Album, Artist

engine = create_engine("sqlite:///mymusic.db",echo=True)

Session = sessionmaker(bind=engine)
session = Session()

new_artist = Artist("Newsbodys")
new_artist.albums = [Album("Read All About It", datetime.date(1988,12,01), "Refuge","CD")]

more_albums = [Album("Hell Is for Wimps",datetime.date(1990,07,31),"Star Song", "CD")]

new_artist.albums.extend(more_albums)

session.add(new_artist)
session.commit()

