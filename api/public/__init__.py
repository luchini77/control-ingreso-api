from fastapi import APIRouter

from api.public.empleado import views as empleados


api = APIRouter()

api.include_router(empleados.router, prefix="/empleados", tags=["Empleados"])