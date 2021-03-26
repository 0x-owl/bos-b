from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from creator import views

urlpatterns = [
    path('list/<str:model_type>', views.generic_model_list, name="list_model"),
    path('detail/<slug:id>/<str:model_name>', views.record_detail, name="record_detail"),
    path('random', views.generate_random_investigator),
    # Core endpoints
    path('<slug:inv>', views.get_investigators_data, name="inv_data"),
    path(
        '<slug:inv>/info',
        views.investigators_basic_info,
        name="basic_info"
    ),
    path(
        '<slug:inv>/attrs',
        views.investigators_attributes,
        name="inv_attrs"
    ),
    path(
        '<slug:inv>/attrs/update',
        views.investigators_attribute_update,
        name="inv_attr_update"
    ),
    path(
        '<slug:inv>/derivative_attrs',
        views.investigators_deriv_attrs,
        name="inv_deriv_attrs"
    ),
    path(
        '<slug:inv>/portrait',
        views.get_investigators_portrait,
        name="inv_portrait"
    ),
    # Skills endpoints
    path(
        '<slug:inv>/skills',
        views.get_investigators_skills,
        name="inv_skills"
    ),
    path(
        '<slug:inv>/skills_update',
        views.update_investigators_skills,
        name="inv_skills_update"
    ),
    path(
        '<slug:inv>/skill_update',
        views.update_investigators_skill,
        name="inv_skill_update"
    ),
    path(
        '<slug:inv>/skills_shuffle',
        views.investigators_skills_shuffle,
        name="inv_skills_shuffle"
    ),
    path(
        '<slug:inv>/skills_reset',
        views.investigators_skills_reset,
        name="inv_skills_reset"
    ),
    # Items endpoints
    path(
        '<slug:inv>/weapons',
        views.get_investigators_weapons,
        name="inv_weapons"
    ),
    path(
        '<slug:inv>/gear',
        views.get_investigators_gear,
        name="inv_gear"
    ),
    path(
        'inventory/<slug:inventory>/remove',
        views.remove_investigators_gear,
        name="inv_gear_remove"
    ),
    path(
        'inventory/<slug:inventory>/edit',
        views.edit_investigators_gear,
        name="inv_gear_edit"
    ),
    # Backstory endpoints
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
        '<slug:inv>/backstory',
        views.get_investigators_backstory,
        name="inv_backstory"
    ),
    path(
        '<slug:inv>/backstory/update',
        views.update_investigators_backstory,
        name="inv_backstory_update"
    ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
