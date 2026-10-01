from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.auth import create_access_token, hash_password, verify_password, get_current_user
from app.database import get_db
from app.models import User
from app.schemas import UserCreate, TokenResponse, UserOut

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user_data.email.lower()).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        name=user_data.name,
        email=user_data.email.lower(),
        password_hash=hash_password(user_data.password),
        role="customer",
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserOut(id=user.id, name=user.name, email=user.email, role=user.role)


@router.post("/login", response_model=TokenResponse)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username.lower()).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id), "role": user.role})
    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return UserOut(id=current_user.id, name=current_user.name, email=current_user.email, role=current_user.role)
