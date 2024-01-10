from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import SportType

admin.site.site_header = 'Data Sport Admin panel'
admin.site.site_title = 'Data Sport  Admin panel'
admin.site.index_title = 'Data Sport  Admin panel'


class SportTypeAdmin(TranslationAdmin):
    list_filter = ('title', 'state',)
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
        ('Ikonka', {'fields': ('icon',)}),
        ('Holati', {'fields': ('state',)}),
    )

admin.site.register(SportType, SportTypeAdmin)