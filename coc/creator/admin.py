from creator.models import (Investigator, InvestigatorAttribute,
                            InvestigatorSkills, Occupation,
                            OccupationAttribute, OccupationSkills, Skills, Tag)
from django.contrib import admin

# Register your models here.
admin.site.register(Investigator)
admin.site.register(InvestigatorAttribute)
admin.site.register(InvestigatorSkills)
admin.site.register(Occupation)
admin.site.register(OccupationAttribute)
admin.site.register(OccupationSkills)
admin.site.register(Skills)
admin.site.register(Tag)
