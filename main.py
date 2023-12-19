from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="FastAPI shop"
)


@app.get("/")
def home():
    return "ok"


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return customer_id


@app.post("/customers/{customer_id}")
def set_customer(customer_id: int, new_name: str):
    return {"status": 200, "data": "ok"}


class Products(BaseModel):
    id: int
    title: str
    description: str
    price: float = Field(ge=0)
    # ge=0 - >=0


@app.post("/products")
def set_product():
    pass
