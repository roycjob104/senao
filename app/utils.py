from fastapi import HTTPException

class AccountValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

class AccountExistsError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class PasswordValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=400, detail=detail)

class AccountNotFoundError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)

class TooManyAttemptsError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=429, detail=detail)