from django.contrib.auth.models import User
import commProd.models as cpm


class EmailOrUsernameBackend(object):

    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {
                'email': username
            }
            user = self.get_user_alt_email(username, password)
            if user:
                return user
        else:
            kwargs = {
                'username': username
            }
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
            Method required to be a valid 
            auth backend
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_user_alt_email(self, email, password):
        """
            allow a user to authenticate
            by any email they have registered
            returns None if no user is found.
        """
        user = cpm.Email.objects.filter(email=email,
                                        confirmed=True)
        if user.exists():
            user = user[0].user_profile.user
            if user.check_password(password):
                return user
        return None
