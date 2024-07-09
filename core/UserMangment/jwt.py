import jwt
from rest_framework.exceptions import AuthenticationFailed


def getUser(request):
    token = request.COOKIES.get('jwt')
    print(token)
    if not token:
        token = request.GET.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        return True, payload

    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')