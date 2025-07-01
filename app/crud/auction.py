from sqlalchemy.orm import Session
from app.db.models.auction import TimeAuction, CourtAuction

# Create Time Auction
def create_time_auction(db: Session, group1_id: int, group2_id: int):
    auction = TimeAuction(group1_id=group1_id, group2_id=group2_id)
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction

# Select time slot
def select_time_slot(db: Session, auction_id: int, group_id: int, slot: str):
    auction = db.query(TimeAuction).filter(TimeAuction.id == auction_id).first()
    if not auction:
        return None

    if group_id == auction.group1_id:
        auction.selected_by_g1 = slot
    elif group_id == auction.group2_id:
        auction.selected_by_g2 = slot
    else:
        return None

    if auction.selected_by_g1 == auction.selected_by_g2 and auction.selected_by_g1:
        auction.finalized_slot = slot
        auction.is_finalized = True

    db.commit()
    db.refresh(auction)
    return auction

# Get time auction status
def get_time_auction_status(db: Session, auction_id: int):
    return db.query(TimeAuction).filter(TimeAuction.id == auction_id).first()


# Court auction
def create_court_auction(db: Session, group1_id: int, group2_id: int):
    auction = CourtAuction(group1_id=group1_id, group2_id=group2_id)
    db.add(auction)
    db.commit()
    db.refresh(auction)
    return auction

def select_court(db: Session, auction_id: int, group_id: int, court_name: str):
    auction = db.query(CourtAuction).filter(CourtAuction.id == auction_id).first()
    if not auction:
        return None

    if group_id == auction.group1_id:
        auction.selected_by_g1 = court_name
    elif group_id == auction.group2_id:
        auction.selected_by_g2 = court_name
    else:
        return None

    if auction.selected_by_g1 == auction.selected_by_g2 and auction.selected_by_g1:
        auction.finalized_court = court_name
        auction.is_finalized = True

    db.commit()
    db.refresh(auction)
    return auction

def get_court_auction_status(db: Session, auction_id: int):
    return db.query(CourtAuction).filter(CourtAuction.id == auction_id).first()
