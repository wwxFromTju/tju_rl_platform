from fastapi import APIRouter, Depends
import psutil

# from ..dependencies import get_token_header
import schemas
from user.user_router import get_current_active_user

router = APIRouter(
    prefix="/sys_info",
    tags=["sys_info"],
    dependencies=[Depends(get_current_active_user)],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=schemas.SysData)
def read_project():
    cpu_count = f'{psutil.cpu_count()} 个核'
    cpu_percent = f'cpu利用率: {psutil.cpu_percent()}%'
    mem =  psutil.virtual_memory()

    M = 1024 * 1024
    G = M * 1024

    mem_total = f'{mem.total / G} G'
    mem_used = f'{mem.used / G} G'
    mem_available = f'{mem.available / G} G'
    mem_percent = f'{mem.percent} %'

    data = schemas.SysData(cpu_count=cpu_count, cpu_percent=cpu_percent, 
    mem_total=mem_total, mem_used=mem_used, mem_available=mem_available, mem_percent=mem_percent)
    return data

