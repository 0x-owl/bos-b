from django.contrib import admin

from market.models import (Content, ContentInvestigator, ContentItem,
                           ContentMania, ContentOccupation, ContentPhobia,
                           ContentSpell, ContentTag, ContentUser, ContentWeapon)

# Register your models here.
admin.site.register(Content)
admin.site.register(ContentInvestigator)
admin.site.register(ContentItem)
admin.site.register(ContentMania)
admin.site.register(ContentOccupation)
admin.site.register(ContentPhobia)
admin.site.register(ContentSpell)
admin.site.register(ContentTag)
admin.site.register(ContentUser)
admin.site.register(ContentWeapon)
