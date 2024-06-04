from sqlalchemy import MetaData, Table, Column, String, BigInteger, Text, ForeignKey, Boolean

metadata = MetaData()

priority_table = Table(
    'priority',
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, unique=True)
)

category_table = Table(
    "category",
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('name', String, nullable=False, default=False),
    Column('created_by_id', BigInteger, ForeignKey('user.id'), nullable=False)
    
)

todo_table = Table(
    "todo",
    metadata,
    Column('id', BigInteger, primary_key=True, autoincrement=True),
    Column('content', Text, nullable=False, default=False),
    Column('user_id', BigInteger, nullable=False),
    Column('is_completed', Boolean, default=False, nullable=False),
    
    Column('priority_id', BigInteger, ForeignKey("priority.id"), nullable=False),
    Column('categoty_id', BigInteger, ForeignKey('category.id'))
)