from typing import Optional
from sqlmodel import Field, SQLModel


class EmpleadoBase(SQLModel):
    nombre: str
    apellidos: str
    rut: str
    email: str
    cargo: str
    empresa: str
    fecha: Optional[str] = None
    hora: Optional[str] = None
    registrado: Optional[bool] = False

    class Config:
        schema_extra = {
            "example": {
                "nombre":"Juan",
                "apellidos":"Perez Gonzalez",
                "rut":"11111111-1",
                "email":"juan@perez.cl",
                "cargo":"M1 OOCC",
                "empresa": "FMT",
                "fecha":"2023-11-09",
                "hora":"12:00:00",
                "registrado": False
            }
        }

class Empleado(EmpleadoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    
class EmpleadoCrear(EmpleadoBase):
    pass 

class EmpleadoLeer(EmpleadoBase):
    id: int
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    rut: Optional[str] = None
    email: Optional[str] = None
    cargo: Optional[str] = None
    empresa: Optional[str] = None
    fecha: Optional[str] = None
    registrado: Optional[bool] = None

class EmpleadoActualizar(EmpleadoBase):
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    rut: Optional[str] = None
    email: Optional[str] = None
    cargo: Optional[str] = None
    empresa: Optional[str] = None
    registrado: Optional[bool] = None