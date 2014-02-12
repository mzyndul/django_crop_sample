from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from crop_widget import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    url('^$', views.ProfileListView.as_view(), name='profile-list'),
    url('^create/$', views.ProfileCreateView.as_view(), name='profile-create'),
    url('^edit/(?P<pk>[\w-]+)$', views.ProfileUpdateView.as_view(), name='profile-update'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
