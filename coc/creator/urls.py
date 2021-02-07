from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path('random', views.generate_random_investigator),
    path('<slug:inv>', views.get_investigators_data, name="inv_data"),
    path(
        '<slug:inv>/sheet',
        views.get_investigators_basic_info,
        name="sheet"
    ),
    path(
        '<slug:inv>/attrs',
        views.get_investigators_attributes,
        name="inv_attrs"
    ),
    path(
        '<slug:inv>/portrait',
        views.get_investigators_portrait,
        name="inv_portrait"
    ),
    path(
        '<slug:inv>/skills',
        views.get_investigators_skills,
        name="inv_skills"
    ),
    path(
        '<slug:inv>/wepons',
        views.get_investigators_weapons,
        name="inv_weapons"
    ),
    path(
        '<slug:inv>/gear',
        views.get_investigators_gear,
        name="inv_gear"
    ),
    path(
        '<slug:inv>/manias_phobias',
        views.get_investigators_manias_and_phobias,
        name="inv_manias_phobias"
    ),
    path(
        '<slug:inv>/arcane',
        views.get_investigators_arcane,
        name="inv_arcane"
    ),
    path(
        '<slug:inv>/derivative_attrs',
        views.get_investigators_deriv_attrs,
        name="inv_deriv_attrs"
    ),
]
