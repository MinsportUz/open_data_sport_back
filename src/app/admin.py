from django.contrib import admin

from .models import SportData

# admin.site.register(SportData)

admin.site.site_header = 'Data Sport Admin panel'
admin.site.site_title = 'Data Sport  Admin panel'
admin.site.index_title = 'Data Sport  Admin panel'


@admin.register(SportData)
class SportDataAdmin(admin.ModelAdmin):
    list_filter = ('title', 'state', 'sport_type', 'created_at')
    search_fields = ('title', 'attr')
    list_per_page = 20
