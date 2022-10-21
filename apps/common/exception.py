from rest_framework import status
from rest_framework.exceptions import APIException


class OlegError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'This is Oleg error'
    default_code = 'oleg_error'
