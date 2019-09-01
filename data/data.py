from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
import os

BASE_DIR = os.path.dirname(__file__)
sqlite_file = os.path.join(BASE_DIR, 'colors.db')
engine = create_engine('sqlite:///' + sqlite_file, echo=True)

Base = declarative_base()


class Colors(Base):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    origin = Column(String(255), nullable=False)
    red = Column(Integer)
    green = Column(Integer)
    blue = Column(Integer)
    hex = Column(String(10))

    def __repr__(self):
        template = "<Colors(name='%s', origin='%s', red='%s', green='%s', blue='%s', hex='%s'>"
        return template % (self.name, self.origin, self.red, self.green, self.blue, self.hex)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
