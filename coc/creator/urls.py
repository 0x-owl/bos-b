from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path('random', views.generate_random_investigator),
    path('<slug:inv>', views.get_investigator_data, name="inv_data"),
    path(
        '<slug:inv>/basic_info',
        views.get_investigator_basic_info,
        name="inv_basic_info"
    ),
    path(
        '<slug:inv>/derivative_attrs',
        views.get_investigator_deriv_attrs,
        name="inv_deriv_attrs"
    ),
]
