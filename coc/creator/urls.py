from django.urls import path

from creator import views

urlpatterns = [
    path('<slug:inv>', views.get_investigator_data),
]