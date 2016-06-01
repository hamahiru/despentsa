import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class StockDespensa(Base):
    __tablename__ = 'despensa'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    kopurua = Column(String (4))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'kopurua' : self.kopurua
        }


engine = create_engine(os.environ['DATABASE_URL'])


Base.metadata.create_all(engine)
