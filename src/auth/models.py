from sqlalchemy import MetaData, Table, Column, String, BigInteger, Boolean
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from ..database import Base

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('username', String, nullable=False),
    Column('email', String, unique=True, nullable=False),
    Column('hashed_password', String(length=320), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False)
)


class User(SQLAlchemyBaseUserTable[int], Base):
    id: int = Column(BigInteger, primary_key=True, autoincrement=True)
    username: str = Column(String(length=320), nullable=False)
    email: str = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)