from django.contrib.auth.models import User

# Authenticate using an e-mail address or username
class EmailAuthBackend(object):
    def authenticate(self, request, username=None, password=None):
        try:
            # uses email or username
            user = User.objects.get(email=username)
            # checks for password stored in the database using hashing system
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None
    # gets the user by its id
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
