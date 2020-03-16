from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page

from saleboxdjango.lib.category import SaleboxCategory
from saleboxdjango.lib.common import get_rating_display
from saleboxdjango.lib.product import SaleboxProduct, translate_path
from saleboxdjango.lib.rating import SaleboxRating
from saleboxdjango.models import AttributeItem, ProductCategory, \
    Product, ProductVariant, ProductVariantImage


class ProductList(RoutablePageMixin, Page):
    subpage_types = []

    @route(r'^')
    def base(self, request):
        print(request.path)