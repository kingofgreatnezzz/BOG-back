from typing import Optional, Tuple
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request) -> Tuple[AuthUser, Token] | None:
        return super().authenticate(request)