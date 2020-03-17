from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.images.views.serve import ServeView

from saleboxdjango.views.account.basket import SaleboxAccountBasketView
from saleboxdjango.views.account.wishlist import SaleboxAccountWishlistView
from saleboxdjango.views.products.products import SaleboxProductsView

from search import views as search_views


urlpatterns = [
    re_path(r'^django-admin/', admin.site.urls),
    re_path(r'^admin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^img/([^/]*)/(\d*)/([^/]*)/[^/]*', ServeView.as_view(), name='wagtailimages_serve'),
]

# these URLs will have /<language_code>/ appended to the beginning
urlpatterns += i18n_patterns(
    # fixed-path items: salebox
    # path('basket/', SaleboxAccountBasketView.as_view()),
    # path('checkout/', include('apps.checkout.urls')),
    # path('salebox/', include('saleboxdjango.urls')),
    # path('wishlist/', SaleboxAccountWishlistView.as_view()),
    re_path(r'shop/(?P<path>.*)', SaleboxProductsView.as_view()),

    # fixed-path items: signup
    # path('signup/', SignUpInitView.as_view()),
    # path('signup/form/', SignUpFormView.as_view()),
    # path('signup/search/', SignUpSearchView.as_view()),
    # path('signup/complete/', SignUpCompleteView.as_view()),
    # path('signup/unset/', unset_sponsor),

    # fixed-path items: inactive users
    # path('account-suspended/', TemplateView.as_view(template_name='account/fbo_inactive.html', extra_context={'fbo_status': 'suspended'})),

    # wagtail search view
    # url(r'^search/$', search_views.search, name='search'),

    # cms
    # path('', include('user.urls')),
    re_path(r'', include(wagtail_urls)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls))
    ]