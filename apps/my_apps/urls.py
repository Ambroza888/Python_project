from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^contact$', views.contact),
    url(r'^reviews$', views.reviews),
    url(r'^taking_review$', views.taking_review),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)