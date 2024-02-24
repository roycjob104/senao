from fastapi import FastAPI, HTTPException
from time import time
from models import Account, Verification
from utils import AccountValidationError, AccountExistsError, PasswordValidationError, AccountNotFoundError, TooManyAttemptsError

app = FastAPI()

# Data storage (temporary solution with in-memory storage)
accounts = []

# Rate limiting (temporary solution with in-memory storage)
attempts = {}

# Constants
PASSWORD_REQUIREMENTS = "Password must be at least 8 characters long, with at least 1 uppercase letter, 1 lowercase letter, and 1 number."
USERNAME_EXISTS = "Username already exists."
ACCOUNT_NOT_FOUND = "Account not found."
TOO_MANY_ATTEMPTS = "Too many attempts. Please try again later."
PASSWORD_IS_NOT_CORRECT = "Incorrect password."
ACCOUNT_REQUIREMENTS = "Username should be between 3 and 32 characters long."

def validate_account(username: str):
    if len(username) < 3 or len(username) > 32:
        raise AccountValidationError(detail=ACCOUNT_REQUIREMENTS)

# Helper functions
def validate_password(password: str):
    if len(password) < 8:
        raise PasswordValidationError(detail="Password is too short.")
    if not any(char.isupper() for char in password):
        raise PasswordValidationError(detail="Password must contain at least one uppercase letter. ")
    if not any(char.islower() for char in password):
        raise PasswordValidationError(detail="Password must contain at least one lowercase letter. ")
    if not any(char.isdigit() for char in password):
        raise PasswordValidationError(detail="Password must contain at least one number. ")

# API endpoints
@app.post("/create-account/")
def create_account(account: Account):
    for acc in accounts:
        if acc.username == account.username:
            return {"success": False, "reason": USERNAME_EXISTS}
    try:
        validate_account(account.username)
        validate_password(account.password)
    except (AccountValidationError, PasswordValidationError) as e:
        return {"success": False, "reason": str(e)}
    
    accounts.append(account)
    return {"success": True}

@app.post("/verify-account/")
def verify_account(verification: Verification):
    for acc in accounts:
        if acc.username == verification.username:
            if attempts.get(verification.username, 0) >= 5:
                raise TooManyAttemptsError(detail=TOO_MANY_ATTEMPTS)
            if acc.password == verification.password:
                attempts[verification.username] = 0
                return {"success": True}
            else:
                attempts[verification.username] = attempts.get(verification.username, 0) + 1
                return {"success": False, "reason": PASSWORD_IS_NOT_CORRECT}
    return {"success": False, "reason": ACCOUNT_NOT_FOUND}
