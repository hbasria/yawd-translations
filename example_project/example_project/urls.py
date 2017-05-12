from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from yawdtrans_demo.views import IndexView, MultilingualPageView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

# insert the url translatable patterns
urlpatterns += [
    url(r'^$', IndexView.as_view(), name='index-view'),
    url(r'^(?P<slug>[\w-]+)/$', MultilingualPageView.as_view(),
        name='multilingual-page-view'),
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
