from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Product, Category
from app.schemas import ProductOut

router = APIRouter()


@router.get("/", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.available == True).all()
    return [
        ProductOut(
            id=p.id,
            name=p.name,
            description=p.description,
            price=float(p.price),
            category_id=p.category_id,
            available=p.available,
            stock_quantity=p.stock_quantity,
        )
        for p in products
    ]


@router.get("/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return ProductOut(
        id=product.id,
        name=product.name,
        description=product.description,
        price=float(product.price),
        category_id=product.category_id,
        available=product.available,
        stock_quantity=product.stock_quantity,
    )
