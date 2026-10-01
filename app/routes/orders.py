from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Review, Shop
from app.schemas import ReviewCreate, ReviewOut
from app.auth import get_current_user

router = APIRouter()


@router.post("/", response_model=ReviewOut)
def create_review(payload: ReviewCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    review = Review(
        user_id=current_user.id,
        shop_id=payload.shop_id,
        product_id=payload.product_id,
        rating=payload.rating,
        title=payload.title or "",
        comment=payload.comment,
        is_verified_purchase=True,
        approved=True,
    )
    db.add(review)
    db.commit()
    db.refresh(review)

    shop = db.query(Shop).filter(Shop.id == payload.shop_id).first()
    if shop:
        reviews = db.query(Review).filter(Review.shop_id == payload.shop_id, Review.approved == True).all()
        avg = sum(r.rating for r in reviews) / len(reviews)
        shop.average_rating = round(avg, 1)
        shop.total_reviews = len(reviews)
        db.commit()

    return ReviewOut(
        id=review.id,
        user_id=review.user_id,
        shop_id=review.shop_id,
        product_id=review.product_id,
        rating=review.rating,
        title=review.title,
        comment=review.comment,
        created_at=review.created_at.isoformat(),
    )


@router.get("/shop/{shop_id}")
def get_shop_reviews(shop_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.shop_id == shop_id, Review.approved == True).order_by(Review.created_at.desc()).all()
    return [
        {
            "id": r.id,
            "user": r.user.name,
            "rating": r.rating,
            "comment": r.comment,
            "title": r.title,
            "created_at": r.created_at.isoformat(),
        }
        for r in reviews
    ]
