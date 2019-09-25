from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
                    
urlpatterns = [
    url(r'^$', views.img_sharing),
    url(r'^uploading_file$', views.uploading_file),
    url(r'^clean_session$', views.clean_session),
    url(r'^reg_in_data$', views.reg_in_data),
    url(r'^log_in_data$', views.log_in_data),
    url(r'^log_reg$', views.log_reg)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)