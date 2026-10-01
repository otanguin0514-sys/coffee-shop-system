from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "sqlite:///./coffee_shop.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


def create_db_and_tables():
    from app import models
    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        # seed shop if empty
        exists = session.execute(text("SELECT 1 FROM shop LIMIT 1")).fetchone()
        if not exists:
            session.execute(
                text(
                    "INSERT INTO shop (name, address, city, phone, opening_hours, average_rating, total_reviews) "
                    "VALUES ('Bean & Bloom Coffee House', '134 Maple Avenue', 'Downtown', '(415) 555-0143', '7am - 9pm', 4.8, 0)"
                )
            )
            session.commit()

        categories = session.execute(text("SELECT COUNT(*) FROM category")).scalar()
        if categories == 0:
            session.execute(
                text(
                    "INSERT INTO category (name, description) VALUES "
                    "('Espresso', 'Strong and rich single-origin shots'), "
                    "('Milk-based', 'Smooth lattes and cappuccinos'), "
                    "('Cold', 'Refreshing cold drinks and iced coffee'), "
                    "('Specialty', 'Signature and seasonal drinks'), "
                    "('Tea', 'Tea and matcha beverages')"
                )
            )
            session.commit()

        products = session.execute(text("SELECT COUNT(*) FROM product")).scalar()
        if products == 0:
            session.execute(
                text(
                    "INSERT INTO product (name, description, price, category_id, stock_quantity, available) VALUES "
                    "('Signature Espresso', 'Bold, smooth, and balanced with a cocoa finish.', 3.50, 1, 50, 1), "
                    "('Cappuccino', 'Velvety milk foam layered over our espresso roast.', 5.25, 2, 40, 1), "
                    "('Vanilla Latte', 'Creamy espresso with vanilla bean sweetness and steamed milk.', 5.95, 2, 35, 1), "
                    "('Mocha Dream', 'Dark chocolate, espresso, and silky milk in one rich cup.', 6.40, 4, 30, 1), "
                    "('Iced Cold Brew', 'Slow-steeped craft coffee with a smooth and refreshing finish.', 4.90, 3, 45, 1), "
                    "('Matcha Cloud', 'Bright ceremonial matcha blended with oat milk and cream foam.', 5.75, 5, 25, 1)"
                )
            )
            session.commit()

        inventory_rows = session.execute(text("SELECT COUNT(*) FROM inventory")).scalar()
        if inventory_rows == 0:
            session.execute(
                text(
                    "INSERT INTO inventory (product_id, stock_level, reorder_level, unit) VALUES "
                    "(1, 82, 5, 'cups'), "
                    "(2, 58, 5, 'cups'), "
                    "(3, 34, 20, 'cups'), "
                    "(4, 29, 20, 'cups'), "
                    "(5, 46, 10, 'cups'), "
                    "(6, 21, 10, 'cups')"
                )
            )
            session.commit()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
