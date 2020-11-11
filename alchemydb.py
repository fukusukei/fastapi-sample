# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

DATABASE = 'postgresql'
PY_DB_LIB = 'psycopg2'
USER = 'fauser'
PASSWORD = 'fauser_password'
HOST = 'db'
PORT = '5432'
DB_NAME = 'fastapi'


Base = declarative_base()
RDB_PATH = '{}+{}://{}:{}@{}:{}/{}'.format(DATABASE, PY_DB_LIB, USER, PASSWORD, HOST, PORT, DB_NAME)
RDB_PATH = 'postgresql+psycopg2://fauser:fauser_password@db:5432/fastapi'
#RDB_PATH = 'sqlite:///db.sqlite3'
ECHO_LOG = False
engine = create_engine(
   RDB_PATH, echo=ECHO_LOG, pool_size=20, max_overflow=0
   #RDB_PATH, echo=ECHO_LOG
)
Session = sessionmaker(bind=engine)
session = Session()