from django.core.cache import cache
from django.db import models

from wagtail.core.models import Page

from saleboxdjango.lib.category import SaleboxCategory
from saleboxdjango.lib.product import SaleboxProduct


class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)

        # fetch categories
        sc = SaleboxCategory()
        context['categories'] = sc.get_tree()

        # fetch products
        sp = SaleboxProduct()
        sp.set_pagination(1, 16, '')
        context['products'] = sp.get_list()

        return context
