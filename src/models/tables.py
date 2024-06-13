from sqlalchemy import MetaData, Table, Column, String, BigInteger, Text, ForeignKey, Boolean
from src.auth.models import user

metadata = MetaData()

priority_table = Table(
    'priority',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True)
)

tag_table = Table(
    'tag',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, default=False),
    Column('user_id', BigInteger, ForeignKey(user.c.id), nullable=False)
    
)

todo_table = Table(
    'todo',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('content', Text, nullable=False, default=False),
    Column('user_id', BigInteger, ForeignKey(user.c.id), nullable=False),
    Column('is_completed', Boolean, default=False, nullable=False),
    
    Column('priority_id', BigInteger, ForeignKey("priority.id"), nullable=False),
    Column('tag_id', BigInteger, ForeignKey('tag.id'))
)