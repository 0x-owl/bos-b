from creator.models import (CampaignInvestigator, Game, Inventory,
                            Investigator, InvestigatorAttribute,
                            InvestigatorsDiary, InvestigatorSkills,
                            InvestigatorTags, Item, ItemImage, ItemTag,
                            Occupation, OccupationAttribute, OccupationSkills,
                            OccupationTags, Portrait, SkillTags, Skills, Spell,
                            SpellTag, SpellType, Tag, TagDiary, Weapon,
                            WeaponImage, WeaponSkill, WeaponTag)
from django.contrib import admin

# Register your models here.
admin.site.register(CampaignInvestigator)
admin.site.register(Game)
admin.site.register(Inventory)
admin.site.register(Investigator)
admin.site.register(InvestigatorAttribute)
admin.site.register(InvestigatorsDiary)
admin.site.register(InvestigatorSkills)
admin.site.register(InvestigatorTags)
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(ItemTag)
admin.site.register(Occupation)
admin.site.register(OccupationAttribute)
admin.site.register(OccupationSkills)
admin.site.register(OccupationTags)
admin.site.register(Portrait)
admin.site.register(Skills)
admin.site.register(SkillTags)
admin.site.register(Spell)
admin.site.register(SpellTag)
admin.site.register(SpellType)
admin.site.register(Tag)
admin.site.register(TagDiary)
admin.site.register(Weapon)
admin.site.register(WeaponImage)
admin.site.register(WeaponSkill)
admin.site.register(WeaponTag)
