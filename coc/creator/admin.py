from creator.models import (Investigator, InvestigatorAttribute,
                            InvestigatorSkills, InvestigatorTags, Occupation,
                            OccupationAttribute, OccupationSkills,
                            OccupationTags, SkillTags, Skills, Spell,
                            SpellType, Tag)
from django.contrib import admin

# Register your models here.
admin.site.register(Investigator)
admin.site.register(InvestigatorAttribute)
admin.site.register(InvestigatorSkills)
admin.site.register(InvestigatorTags)
admin.site.register(Occupation)
admin.site.register(OccupationAttribute)
admin.site.register(OccupationSkills)
admin.site.register(OccupationTags)
admin.site.register(Skills)
admin.site.register(SkillTags)
admin.site.register(Spell)
admin.site.register(SpellType)
admin.site.register(Tag)
