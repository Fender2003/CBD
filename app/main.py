# Entry point (runs FastAPI app)
from fastapi import FastAPI
from app.api.v1 import users
from app.db.base import Base
from app.db.session import engine
import traceback

app = FastAPI(debug=True)

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

try:
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
except Exception:
    print("Database initialization failed")
    traceback.print_exc()
