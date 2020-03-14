from django.contrib import admin

from saleboxdjango.admin import SaleboxUserAdmin
from .models import User

admin.site.register(User, SaleboxUserAdmin)
