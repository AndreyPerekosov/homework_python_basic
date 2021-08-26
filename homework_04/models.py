"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declared_attr, declarative_base, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"


class Base:
    __mapper_args__ = {'eager_defaults': True}

    @declared_attr
    def __tablename__(cls):
        return f"post_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base(cls=Base, bind=engine)


class User(Base):
    name = Column(String(64), nullable=False)
    username = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"name={self.name!r}, username={self.username!r},"
            f"email={self.email!r}"
        )

    def __repr__(self):
        return str(self)


class Post(Base):
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")

    user_id = Column(Integer, ForeignKey("post_users.id"), nullable=False)
    user = relationship("User", back_populates="posts")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}), "
            f"title={self.title!r}, user_id={self.user_id}"

        )

    def __repr__(self):
        return str(self)


# expire_on_commit=False will prevent attributes from being expired
# after commit.
Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def create_tables():
    """
    Creating tables in async mode
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    # close and clean-up pooled connection
    await engine.dispose()
