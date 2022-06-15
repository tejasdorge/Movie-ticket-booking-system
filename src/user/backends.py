from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth import get_user_model

class AuthentificationBackend(ModelBackend):
    """
    Define a new authentification backend for auth with phone_number/password or email/password.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        USER = get_user_model()
        if username is None:
            username = kwargs.get(USER.USERNAME_FIELD)
        try:
            user = USER.objects.get(
                 Q(email=username) | Q(phone_number=username)
            )
            password_valid = user.check_password(password)
            if password_valid:
                return user
            return None
        except USER.DoesNotExist:
            return None
