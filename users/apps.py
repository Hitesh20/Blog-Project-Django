from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

#this is to run the signals file in order to get our profile saved
    def ready(self):
        import users.signals