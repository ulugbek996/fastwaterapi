import jwt
from fastapi import HTTPException , Security
from fastapi.security import HTTPAuthorizationCredentials , HTTPBearer
from passlib.context import CryptContext
from  datetime import datetime , timedelta


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = 'SECRET'

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)


    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)



