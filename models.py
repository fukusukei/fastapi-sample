# -*- coding: utf-8 -*-
import os
from alchemydb import Base, engine
from sqlalchemy import Column, Integer, String, Text, text, DateTime
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime

class Tasks(Base):
    __tablename__ = 'tasks'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(256))
    text = Column(String(256))
    created_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        default=datetime.now(),
        nullable=False,
        onupdate=datetime.now()
        # server_default=text(
        #     'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'
        # )
    )

if __name__ == "__main__":
    Base.metadata.create_all(engine)