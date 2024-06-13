from fastapi_users.openapi import OpenAPIResponseType
from src.utils.responses import get_open_api_response

def bad_request() -> OpenAPIResponseType:
    return get_open_api_response(
        {
            'Trying to add an existing tag': 'tag name already exists'
        }
    )


def forbidden() -> OpenAPIResponseType:
    return get_open_api_response(
        {
            'Trying to delete system or another users tag':
            'a user can not delete a tag that was not created by him'
        }
    )


def not_found() -> OpenAPIResponseType:
    return get_open_api_response(
        {   
            'Trying to delete/update non existing tag': 'tag does not exists'
        }
    )