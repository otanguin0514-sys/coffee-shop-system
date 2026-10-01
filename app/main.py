from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

from app.database import create_db_and_tables
from app.routes import products, reviews, orders, inventory, admin, auth

app = FastAPI(title="Bean & Bloom Coffee Shop", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(reviews.router, prefix="/api/reviews", tags=["reviews"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["inventory"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])

frontend_dir = Path(__file__).resolve().parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=str(frontend_dir)), name="static")

@app.on_event("startup")
def startup_event():
    create_db_and_tables()

@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Bean & Bloom API is running"}

@app.get("/")
def serve_frontend():
    return FileResponse(frontend_dir / "index.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
