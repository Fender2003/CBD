# Entry point (runs FastAPI app)
from fastapi import FastAPI
from app.api.v1 import users
from app.db.base_class import Base
from app.db.session import engine
from app.api.v1 import groups
from app.db.models import court_owner, user, group, group_card, group_player, court_owner
from app.api.v1 import match
from app.api.v1 import court
from app.api.v1 import sport
from app.api.v1 import group_match_request
from app.api.v1 import lobby_system
from app.api.v1 import court_owner
from app.api.v1 import arena

import traceback

app = FastAPI(debug=True)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
app.include_router(match.router, prefix="/api/v1", tags=["match"])
app.include_router(lobby_system.router, prefix="/api/v1", tags=["lobby"])
app.include_router(group_match_request.router, prefix="/api/v1", tags=["matchRequest"])
app.include_router(sport.router, prefix="/api", tags=["sport"])
# app.include_router(court.router, prefix="/api/v1", tags=["court"])



app.include_router(court_owner.router, prefix="/api/v1", tags=["ownerLogin"])
app.include_router(arena.router, prefix="/api/v1", tags=["Add Arena"])



try:
    # print("Dropping all tables...")
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
except Exception:
    print("Database initialization failed")
    traceback.print_exc()