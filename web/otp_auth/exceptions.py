from rest_framework.exceptions import APIException


class InvalidPhoneNumberException(APIException):
    status_code = 400
