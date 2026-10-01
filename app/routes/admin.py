from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Inventory, Product
from app.auth import get_current_user

router = APIRouter()


@router.get("/")
def get_inventory(db: Session = Depends(get_db)):
    inventory = db.query(Inventory).all()
    return [
        {
            "id": inv.id,
            "product_id": inv.product_id,
            "product_name": inv.product.name,
            "stock_level": inv.stock_level,
            "reorder_level": inv.reorder_level,
            "unit": inv.unit,
        }
        for inv in inventory
    ]


@router.get("/low-stock")
def get_low_stock(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Access denied")

    inventory = db.query(Inventory).filter(Inventory.stock_level <= Inventory.reorder_level).all()
    return [
        {
            "id": inv.id,
            "product_name": inv.product.name,
            "stock_level": inv.stock_level,
            "reorder_level": inv.reorder_level,
        }
        for inv in inventory
    ]
