from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path('random', views.generate_random_investigator),
    path('<slug:inv>', views.get_investigator_data),
]