from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import SportData

admin.site.site_header = 'Data Sport Admin panel'
admin.site.site_title = 'Data Sport  Admin panel'
admin.site.index_title = 'Data Sport  Admin panel'


class SportDataAdmin(TranslationAdmin):
    list_filter = ('title', 'state', 'sport_type', 'created_at')
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
        ('Manzil', {'fields': ('youtube url',)}),
        ('file', {'fields': ('file',)}),
        ('Ko\'rishlar soni', {'fields': ('views',)}),
        ('Yaratilgan vaqti', {'fields': ('created_at',)}),
        ('Tahrirlangan vaqti', {'fields': ('updated_at',)}),
        ('Chop etilgan vaqti', {'fields': ('published_at',)}),
        ('Holati', {'fields': ('state',)}),
        ('Sport turi', {'fields': ('sport_type',)}),
    )


admin.site.register(SportData, SportDataAdmin)