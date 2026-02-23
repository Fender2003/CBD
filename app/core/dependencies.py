from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.security import ALGORITHM, SECRET_KEY
from app.crud import user as crud_user
from app.db.models.user import User
from app.db.session import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise credentials_exception from exc

    subject = payload.get("sub")
    email = payload.get("email")

    user = None
    if subject:
        try:
            user_id = UUID(str(subject))
            user = crud_user.get_user_by_id(db, user_id)
        except ValueError:
            user = crud_user.get_user_by_email(db, str(subject))

    if user is None and email:
        user = crud_user.get_user_by_email(db, str(email))

    if user is None:
        raise credentials_exception

    return user
