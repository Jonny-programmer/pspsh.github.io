from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

# class AdultUser(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, unique=True)
#
#     name = Column(String, nullable=False)
#     surname = Column(String, nullable=False)
#     patronymic = Column(String, nullable=True)
#
#     nickname = Column(String, nullable=False, unique=True, index=True, default=f"user_{uuid.uuid1()}")
#
#     last_seen = Column(DateTime, default=datetime.now)
#     birth_date = Column(DateTime, nullable=False)
#
#     email = Column(String, nullable=False)
#
#     profile_pic = Column(String, nullable=True)
#     hashed_password = Column(String, nullable=True)
#
#     def set_password(self, password):
#         self.hashed_password = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.hashed_password, password)
