from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.


class BaseUser(AbstractBaseUser):
    def get_short_name(self):
        pass

    def get_full_name(self):
        pass
