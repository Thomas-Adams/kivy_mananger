from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Text

engine = create_engine('postgresql+psycopg2://tadams:+Laurin+00+@localhost/colors')

Base = declarative_base()


class Colors(Base):
    __tablename__ = 'colors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    origin = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    red = Column(Integer, nullable=False)
    green = Column(Integer, nullable=False)
    blue = Column(Integer, nullable=False)
    hex = Column(String(10), nullable=False)
    description = Column(Text)
    filename = Column(String(255))

    def __repr__(self):
        template = "<Colors(name='%s', origin='%s',title='%s', red='%s', green='%s', blue='%s', hex='%s'>"
        return template % (self.name, self.origin, self.title, self.red, self.green, self.blue, self.hex)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
