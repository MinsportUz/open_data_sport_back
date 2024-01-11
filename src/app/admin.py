from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import SportData, LegislativeDocument

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
        ('Youtube url', {'fields': ('url',)}),
        ('File', {'fields': ('file',)}),
        ('Rasm', {'fields': ('image',)}),
        ('Muallif', {'fields': ('author',)}),
        ('Nashriyot', {'fields': ('publisher',)}),
        ('Chop etilgan vaqti', {'fields': ('published_at',)}),
        ('Holati', {'fields': ('state',)}),
        ('Sport turi', {'fields': ('sport_type',)}),
        ('Tili', {'fields': ('language',)}),
    )
    _orig_was_required = {
        'title_uz': True,
        'title_en': True,
        'title_ru': True,
    }


class LegislativeDocumentAdmin(TranslationAdmin):
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'attr')
    list_per_page = 20

    fieldsets = (
        ('O\'zbekcha', {'fields': ('title_uz', 'attr_uz',)}),
        ('Inglizcha', {'fields': ('title_en', 'attr_en',)}),
        ('Ruscha', {'fields': ('title_ru', 'attr_ru',)}),
        ('Lex url', {'fields': ('url',)}),
        ('Xolati', {'fields': ('state',)}),
    )


admin.site.register(SportData, SportDataAdmin)
admin.site.register(LegislativeDocument, LegislativeDocumentAdmin)
