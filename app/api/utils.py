from rest_framework.views import exception_handler
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if isinstance(exc, MethodNotAllowed):
        response.data = {'detail': 'This HTTP method is not allowed on this endpoint.'}
        response.status_code = 405
    
    return response