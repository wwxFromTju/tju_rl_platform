from fastapi import APIRouter, Depends
import psutil
import GPUtil

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
    info_dict = dict()

    # CPU
    info_dict["cpu_count"] = f'{psutil.cpu_count()} 个核'
    info_dict["cpu_percent"] = f'cpu利用率: {psutil.cpu_percent()}%'
    
    # Memory
    mem =  psutil.virtual_memory()
    M = 1024 * 1024
    G = M * 1024

    info_dict["mem_total"] = f'{mem.total / G} G'
    info_dict["mem_used"] = f'{mem.used / G} G'
    info_dict["mem_available"] = f'{mem.available / G} G'
    info_dict["mem_percent"] = f'{mem.percent} %'

    # gpu_id_list: Optional[list] = None
    # gpu_name_dict: Optional[Dict] = None
    # gpu_load_dict: Optional[Dict] = None
    # gpu_free_memory_dict: Optional[Dict] = None
    # gpu_used_memory_dict: Optional[Dict] = None
    # gpu_total_memory_dict: Optional[Dict] = None
    # gpu_temperature_dict: Optional[Dict] = None

    # GPU
    gpus = GPUtil.getGPUs()
    if gpus:
        info_dict["gpu_id_list"] = []
        info_dict["gpu_name_dict"] = dict()
        info_dict["gpu_load_dict"] = dict()
        info_dict["gpu_free_memory_dict"] = dict()
        info_dict["gpu_used_memory_dict"] = dict()
        info_dict["gpu_total_memory_dict"] = dict()
        info_dict["gpu_temperature_dict"] = dict()
        
        for gpu in gpus:
            # get the GPU id
            info_dict["gpu_id_list"].append(gpu.id)
            # name of GPU
            info_dict["gpu_name_dict"][gpu.id] = gpu.name
            # get % percentage of GPU usage of that GPU
            info_dict["gpu_load_dict"][gpu.id] = f"{gpu.load*100}%"
            # get free memory in MB format
            info_dict["gpu_free_memory_dict"][gpu.id] = f"{gpu.memoryFree}MB"
            # get used memory
            info_dict["gpu_used_memory_dict"][gpu.id] = f"{gpu.memoryUsed}MB"
            # get total memory
            info_dict["gpu_total_memory_dict"][gpu.id] = f"{gpu.memoryTotal}MB"
            # get GPU temperature in Celsius
            info_dict["gpu_temperature_dict"][gpu.id] = f"{gpu.temperature} °C"
      
    data = schemas.SysData(**info_dict)
    return data

