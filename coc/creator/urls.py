from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path('<slug:inv>', views.get_investigator_data),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)