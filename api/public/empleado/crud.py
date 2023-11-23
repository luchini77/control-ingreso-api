from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select, col
from datetime import datetime

from api.database import get_session
from api.public.empleado.models import Empleado, EmpleadoCrear, EmpleadoActualizar


def fecha_actual():
    fecha = datetime.today()
    date = fecha.strftime("%d/%m/%Y")
    return date
    

def hora_actual():
    hora = datetime.now()
    time = hora.strftime("%H:%M:%S")
    return time


def get_empleados(db:Session=Depends(get_session)):
    empleados = db.exec(select(Empleado)).all()
    return empleados


def create_empleado(empleado:EmpleadoCrear,db:Session=Depends(get_session)):
    new_empleado = Empleado.from_orm(empleado)
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado


def get_by_id(id:int,db:Session=Depends(get_session)):
    empleado = db.get(Empleado,id)

    if not empleado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra empleado con ese id: {id}')
    return empleado


def get_by_rut(rut:str,db:Session=Depends(get_session)):
    result = select(Empleado).where(Empleado.rut == rut)
    data = db.exec(result)

    activo = data.one()

    if not activo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra empleado con ese rut: {rut}')

    if activo.registrado == False:
        activo.registrado = True
    else:
        activo.registrado = False

    activo.fecha = fecha_actual()
    activo.hora = hora_actual()
  

    db.add(activo)
    db.commit()
    return activo

def get_by_registrado(db:Session=Depends(get_session)):
    res = select(Empleado).where(col(Empleado.registrado) == True)
    data = db.exec(res)
    empleados = data.all()
    
    return empleados


def update_empleado(id:int,empleado:EmpleadoActualizar,db:Session=Depends(get_session)):

    empleado_update = db.get(Empleado,id)
    if not empleado_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra empleado con ese id: {id}')
    
    empleado_data = empleado.dict(exclude_unset=True)

    for key,value in empleado_data.items():
        setattr(empleado_update,key,value)

    db.add(empleado_update)
    db.commit()
    db.refresh(empleado_update)
    return empleado_update


def delete_empleado(id:int,db:Session=Depends(get_session)):
    seleccion = select(Empleado).where(Empleado.id == id)

    if seleccion is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No se encuentra empleado con ese id: {id}')
    
    res = db.exec(seleccion)
    empleado = res.one()

    print(empleado)
    
    db.delete(empleado)
    db.commit()
    return {"Empleado borrado": True}
