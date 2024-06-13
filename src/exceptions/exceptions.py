from typing import Callable, Type
from fastapi import status, HTTPException
from functools import wraps

from src.exceptions.resource_already_exist import ResourceAlreadyExist
from src.exceptions.resource_not_exist import ResourceNotExist

exception_map: dict[Type[Exception], int] = {
    ValueError: status.HTTP_400_BAD_REQUEST,
    ResourceNotExist: status.HTTP_404_NOT_FOUND,
    ResourceAlreadyExist: status.HTTP_409_CONFLICT,
}

exceptions: tuple[Type[Exception]] = tuple(exception_map.keys())


async def exeption_handler(func: Callable):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)  
        except exceptions as ex:
            raise HTTPException(status_code=exception_map[type(ex)], detail=str(ex))     
    return wrapper