from fastapi import APIRouter, Depends
from typing import List
from sqlmodel import Session

from api.database import get_session
from api.public.empleado.models import EmpleadoCrear, EmpleadoLeer, EmpleadoActualizar
from api.public.empleado.crud import (get_empleados, get_by_id, get_by_rut,get_by_registrado, create_empleado, update_empleado, delete_empleado)


router = APIRouter()


@router.get("", response_model=List[EmpleadoLeer])
def leer_empleados(db:Session=Depends(get_session)):
    return get_empleados(db=db)


@router.post("", response_model=EmpleadoLeer)
def crear_empleado(empleado:EmpleadoCrear,db:Session=Depends(get_session)):
    return create_empleado(empleado=empleado,db=db)


@router.get("/{id}", response_model=EmpleadoLeer)
def leer_empleado(id:int,db:Session=Depends(get_session)):
    return get_by_id(id=id,db=db)


@router.get("/rut/{rut}", response_model=EmpleadoLeer)
def leer_empleado_rut(rut:str,db:Session=Depends(get_session)):
    return get_by_rut(rut=rut,db=db)

@router.get("/", response_model=List[EmpleadoLeer])
def leer_empleados_registrados(db:Session=Depends(get_session)):
    return get_by_registrado(db=db)


@router.patch("/{id}", response_model=EmpleadoLeer)
def actualizar_empleado(id:int,empleado:EmpleadoActualizar,db:Session=Depends(get_session)):
    return update_empleado(id=id,empleado=empleado,db=db)


@router.delete("/{id}")
def borrar_empleado(id:int,db:Session=Depends(get_session)):
    return delete_empleado(id=id,db=db)