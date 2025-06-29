# Entry point (runs FastAPI app)
from fastapi import FastAPI
from app.api.v1 import users
from app.db.base_class import Base
from app.db.session import engine
from app.api.v1 import groups
from app.db.models import user, group, group_card, group_player
from app.api.v1 import match

import traceback

app = FastAPI(debug=True)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["groups"])
app.include_router(match.router, prefix="/api/v1", tags=["match"])

try:
    print("Dropping all tables...")
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
except Exception:
    print("Database initialization failed")
    traceback.print_exc()
