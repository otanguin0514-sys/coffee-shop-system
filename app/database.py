from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product, Inventory, Review, Order
from app.auth import get_current_user
from app.schemas import ProductBase

router = APIRouter()


@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Admin access required")

    today_orders = db.query(Order).count()
    revenue = sum(float(o.order_total) for o in db.query(Order).all())
    low_stock = db.query(Inventory).filter(Inventory.stock_level <= Inventory.reorder_level).count()
    avg_rating = db.query(Review).with_entities(Review.rating).all()
    avg = sum(r[0] for r in avg_rating) / len(avg_rating) if avg_rating else 0

    return {
        "orders_today": today_orders,
        "revenue_today": round(revenue, 2),
        "low_stock_items": low_stock,
        "average_rating": round(avg, 1) if avg else 0,
    }


@router.post("/products")
def create_product(payload: ProductBase, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Admin access required")

    product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        category_id=payload.category_id,
        stock_quantity=payload.stock_quantity,
        available=payload.available,
    )
    db.add(product)
    db.commit()
    db.refresh(product)

    inventory = Inventory(
        product_id=product.id,
        stock_level=payload.stock_quantity,
        reorder_level=5,
        unit="cups",
    )
    db.add(inventory)
    db.commit()

    return {"message": "Product created", "product_id": product.id}
