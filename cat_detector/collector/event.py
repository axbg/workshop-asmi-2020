from db import Base
from sqlalchemy import Column, Integer, TIMESTAMP

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    timestamp = Column(TIMESTAMP)
    duration = Column(Integer)

    def __init__(self, timestamp, duration):
        self.timestamp = timestamp
        self.duration = duration

    def to_json(self):
        timestamp = "{}-{}-{}#{}:{}".format(self.timestamp.day, self.timestamp.month, self.timestamp.year, self.timestamp.hour, self.timestamp.minute if self.timestamp.minute > 9 else "0" + str(self.timestamp.minute))
        
        return { "id": self.id, "timestamp": timestamp, "duration": self.duration }