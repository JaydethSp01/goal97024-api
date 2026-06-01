from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    categoria_id: int
    talla: str
    proveedor_id: int

class Categoria(BaseModel):
    id: int
    nombre: str

class Proveedor(BaseModel):
    id: int
    nombre: str
    contacto: str

class Stock(BaseModel):
    producto_id: int
    talla: str
    cantidad: int

class Alerta(BaseModel):
    producto_id: int
    talla: str
    cantidad_min: int
    notificado: bool