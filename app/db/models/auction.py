from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.db.base import Base

class TimeAuction(Base):
    __tablename__ = "time_auctions"

    id = Column(Integer, primary_key=True)
    group1_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group2_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    selected_by_g1 = Column(String, nullable=True)
    selected_by_g2 = Column(String, nullable=True)
    finalized_slot = Column(String, nullable=True)
    is_finalized = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class CourtAuction(Base):
    __tablename__ = "court_auctions"

    id = Column(Integer, primary_key=True)
    group1_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    group2_id = Column(Integer, ForeignKey("group.id"), nullable=False)
    selected_by_g1 = Column(String, nullable=True)  # e.g., "United Court"
    selected_by_g2 = Column(String, nullable=True)
    finalized_court = Column(String, nullable=True)
    is_finalized = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    