# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, Table
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


t_character_rules = Table(
    'character_rules', metadata,
    Column('c_id', Numeric(8, 0), primary_key=True, nullable=False),
    Column('ru_id', Numeric(8, 0), primary_key=True, nullable=False)
)


t_room_user = Table(
    'room_user', metadata,
    Column('userid', Numeric(8, 0), primary_key=True, nullable=False),
    Column('roomid', Numeric(8, 0), primary_key=True, nullable=False)
)


class TCharacterSheet(Base):
    __tablename__ = 't_character_sheet'

    c_id = Column(Numeric(8, 0), primary_key=True)
    userid = Column(Numeric(8, 0))
    c_name = Column(String(128))
    c_create_time = Column(DateTime)
    c_file_add = Column(String(128))


class TRoom(Base):
    __tablename__ = 't_room'

    roomid = Column(Numeric(8, 0), primary_key=True)
    userid = Column(Numeric(8, 0))
    room_num = Column(String(9))
    room_rules = Column(Numeric(8, 0))
    room_name = Column(String(23))
    room_file_add = Column(String(66))


class TRule(Base):
    __tablename__ = 't_rules'

    ru_id = Column(Numeric(8, 0), primary_key=True)
    userid = Column(Numeric(8, 0))
    ru_name = Column(Numeric(8, 0))
    ru_father = Column(Numeric(8, 0))
    ru_short = Column(String(128))
    ru_file_add = Column(String(128))


class TUser(Base):
    __tablename__ = 't_user'

    userid = Column(Numeric(8, 0), primary_key=True)
    user_type = Column(String(16))
    user_password = Column(String(18), nullable=False)
    username = Column(String(19))
    user_email = Column(String(25))
