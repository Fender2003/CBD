# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.dialects.postgresql import UUID
# import uuid

# from sqlalchemy.orm import relationship
# from app.db.base_class import Base

# class Player(Base):
#     __tablename__ = "players"

#     player_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
#     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     phone_num = Column(String, unique=True, nullable=False)
#     gender = Column(String, nullable=False)
#     age = Column(Integer, nullable=False)
#     city = Column(String, nullable=True)
#     state = Column(String, nullable=True)

#     user = relationship("User")