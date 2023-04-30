from rest_framework.authentication import TokenAuthentication as BaseToken


class TokenAuthentication(BaseToken):
    # TODO: Find a way that token refresh by deleting after certain time
    keyword = 'Token'
