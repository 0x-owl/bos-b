from creator.models import (Inventory, Investigator, InvestigatorAttribute,
                            InvestigatorSkills, InvestigatorTags, Item,
                            ItemTag, Occupation, OccupationAttribute,
                            OccupationSkills, OccupationTags, SkillTags,
                            Skills, Spell, SpellTag, SpellType, Tag)
from django.contrib import admin

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Investigator)
admin.site.register(InvestigatorAttribute)
admin.site.register(InvestigatorSkills)
admin.site.register(InvestigatorTags)
admin.site.register(Item)
admin.site.register(ItemTag)
admin.site.register(Occupation)
admin.site.register(OccupationAttribute)
admin.site.register(OccupationSkills)
admin.site.register(OccupationTags)
admin.site.register(Skills)
admin.site.register(SkillTags)
admin.site.register(Spell)
admin.site.register(SpellTag)
admin.site.register(SpellType)
admin.site.register(Tag)
