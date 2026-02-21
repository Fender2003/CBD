# Entry point (runs FastAPI app)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import users
from app.db.base_class import Base
from app.db.session import engine
from app.api.v1 import groups
from app.db.models import court_owner, user, group, group_card, group_player, court_owner
from app.api.v1 import match
from app.api.v1 import sport
from app.api.v1 import group_match_request
from app.api.v1 import lobby_system
from app.api.v1 import court_owner
from app.api.v1 import arena
from app.api.v1 import wins_losses
from app.api.v1 import completed_game


import traceback

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "docs": "/docs"}

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
app.include_router(lobby_system.router, prefix="/api/v1", tags=["lobby"])
app.include_router(match.router, prefix="/api/v1", tags=["match"])
app.include_router(group_match_request.router, prefix="/api/v1", tags=["matchRequest"])
app.include_router(completed_game.router, prefix="/api/v1", tags=["Game Finalize"])



app.include_router(sport.router, prefix="/api", tags=["sport"])



app.include_router(court_owner.router, prefix="/api/v1", tags=["ownerLogin"])
app.include_router(arena.router, prefix="/api/v1", tags=["Add Arena"])
app.include_router(wins_losses.router, prefix="/api/v1", tags=["Add Game stats"])


try:
    # print("Dropping all tables...")
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
except Exception:
    print("Database initialization failed")
    traceback.print_exc()
