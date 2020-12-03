from db import Base
from sqlalchemy import Column, Integer, TIMESTAMP
from sqlalchemy.ext.hybrid import hybrid_property


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    duration = Column(Integer)

    def __init__(self, timestamp, duration):
        self.timestamp = timestamp
        self.duration = duration
