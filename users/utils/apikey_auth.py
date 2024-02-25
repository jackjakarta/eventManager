from rest_framework_api_key.permissions import BaseHasAPIKey

from users.models import UserAPIKey


class UserHasAPIKey(BaseHasAPIKey):
    model = UserAPIKey
