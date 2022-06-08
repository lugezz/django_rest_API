from ast import keyword
from rest_framework.authentication import TokenAuthentication as BaseToken

class TokenAuthentication(BaseToken):
    keyword = 'Bearer'

