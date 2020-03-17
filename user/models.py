from django.db import models
from django.utils.translation import gettext_lazy as _

from saleboxdjango.models import SaleboxUser


class User(SaleboxUser):
    username = models.CharField(_('username'), max_length=150, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # this is here so createsuperuser works

    def __str__(self):
        return self.email