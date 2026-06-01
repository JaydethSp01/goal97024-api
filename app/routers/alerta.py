from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Alerta(BaseModel):
    id: int
    producto: str
    talla: str
    cantidad: int
    mensaje: str

alertas_db = [
    Alerta(id=1, producto="Camiseta", talla="M", cantidad=5, mensaje="Stock bajo"),
    Alerta(id=2, producto="Pantalón", talla="L", cantidad=2, mensaje="Últimas unidades")
]

@router.get("/alerta", response_model=List[Alerta])
async def get_alertas():
    return alertas_db

@router.post("/alerta", response_model=Alerta)
async def create_alerta(alerta: Alerta):
    alertas_db.append(alerta)
    return alerta

@router.get("/alerta/{alerta_id}", response_model=Alerta)
async def get_alerta(alerta_id: int):
    alerta = next((al for al in alertas_db if al.id == alerta_id), None)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    return alerta

@router.put("/alerta/{alerta_id}", response_model=Alerta)
async def update_alerta(alerta_id: int, updated_alerta: Alerta):
    for index, alerta in enumerate(alertas_db):
        if alerta.id == alerta_id:
            alertas_db[index] = updated_alerta
            return updated_alerta
    raise HTTPException(status_code=404, detail="Alerta not found")

@router.delete("/alerta/{alerta_id}", response_model=Alerta)
async def delete_alerta(alerta_id: int):
    alerta = next((al for al in alertas_db if al.id == alerta_id), None)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta not found")
    alertas_db.remove(alerta)
    return alerta
