from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria: str

productos_db = [
    Producto(id=1, nombre="Camiseta", precio=19.99, categoria="Ropa"),
    Producto(id=2, nombre="Pantalón", precio=29.99, categoria="Ropa")
]

@router.get("/producto", response_model=List[Producto])
async def get_productos():
    return productos_db

@router.post("/producto", response_model=Producto)
async def create_producto(producto: Producto):
    productos_db.append(producto)
    return producto

@router.get("/producto/{producto_id}", response_model=Producto)
async def get_producto(producto_id: int):
    producto = next((prod for prod in productos_db if prod.id == producto_id), None)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return producto

@router.put("/producto/{producto_id}", response_model=Producto)
async def update_producto(producto_id: int, updated_producto: Producto):
    for index, producto in enumerate(productos_db):
        if producto.id == producto_id:
            productos_db[index] = updated_producto
            return updated_producto
    raise HTTPException(status_code=404, detail="Producto not found")

@router.delete("/producto/{producto_id}", response_model=Producto)
async def delete_producto(producto_id: int):
    producto = next((prod for prod in productos_db if prod.id == producto_id), None)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    productos_db.remove(producto)
    return producto
