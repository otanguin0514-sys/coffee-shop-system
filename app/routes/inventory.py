from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Order, OrderItem, Product
from app.schemas import OrderCreate
from app.auth import get_current_user

router = APIRouter()


@router.post("/")
def create_order(payload: OrderCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if not payload.items:
        raise HTTPException(status_code=400, detail="Order must contain at least one item")

    total = 0
    for item in payload.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product {item.product_id} not found")
        if product.stock_quantity < item.quantity:
            raise HTTPException(status_code=400, detail=f"Not enough stock for {product.name}")
        total += float(product.price) * item.quantity

    order = Order(
        user_id=current_user.id,
        shop_id=1,
        order_number=f"ORD-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        order_total=round(total, 2),
        status="pending",
        payment_method=payload.payment_method,
        notes=payload.notes,
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    for item in payload.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        order_item = OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=product.price,
        )
        db.add(order_item)
        product.stock_quantity -= item.quantity

    db.commit()
    return {"message": "Order created successfully", "order_id": order.id, "total": round(total, 2)}


@router.get("/")
def get_my_orders(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    orders = db.query(Order).filter(Order.user_id == current_user.id).order_by(Order.created_at.desc()).all()
    return [{
        "id": o.id,
        "order_number": o.order_number,
        "status": o.status,
        "total": float(o.order_total),
        "created_at": o.created_at.isoformat(),
    } for o in orders]
