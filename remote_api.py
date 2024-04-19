from fastapi import APIRouter
from remote_tools import Statistics
api = APIRouter()


@api.get("/cpu")
async def get_cpu(self=None):
    cpu_data = Statistics.cpu_usage(self)
    return f'{cpu_data}'

@api.get("/disk")
async def get_disk(self=None):
    disk_data = Statistics.disk_usage(self)
    return f'{disk_data}'


@api.get("/mem")
async def get_memory(self=None):
    mem_data = Statistics.mem_usage(self)
    return f'{mem_data}'
