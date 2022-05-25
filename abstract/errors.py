from enum import Enum
from rest_framework.exceptions import ValidationError


class CodeErrors(Enum):
    INCORRET_VALUE = {1: 400}
    NOT_FOUND = {2: 404}
    NOT_MATCH = {3: 400}
    NOT_ACTIVE = {4: 403}
    MISSING_VALUE = {5: 400}
    PENDING = {6: 400}


class ErrorExceptionFactory:

    def __init__(self, code: int, component: str, msg: str):

        self._code = code,
        self.code = ""
        self.component = component
        self.msg = msg

    def raise_exception(self):
        pass

