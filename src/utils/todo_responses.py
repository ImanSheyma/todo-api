from fastapi_users.openapi import OpenAPIResponseType
from src.utils.responses import get_open_api_response

def bad_request() -> OpenAPIResponseType:
    return get_open_api_response(
        {
            'Trying to connect duplicate categories or another users category': 'categories are not valid',
            'Trying to connect non existing priority': 'priority is not valid'
        }
    )


def forbidden() -> OpenAPIResponseType:
    return get_open_api_response(
        {
            'Trying to update another users todo':
            'a user can not update a todo that was not created by him'
        }
    )


def not_found() -> OpenAPIResponseType:
    return get_open_api_response(
        {   
            'Trying to update non existing todo': 'todo does not exists'
        }
    )