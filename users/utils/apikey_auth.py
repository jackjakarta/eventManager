from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import UserAPIKey


class CustomAPIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-Api-Key')

        if api_key:
            try:
                user_api_key = UserAPIKey.objects.get_from_key(api_key)

                if user_api_key:
                    return user_api_key.user, user_api_key
            except UserAPIKey.DoesNotExist:
                raise AuthenticationFailed('Invalid API key')

        return None

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True
