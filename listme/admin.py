from django.contrib import admin
from listme.models import List, ListElement


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_list', 'is_public')
    search_fields = ('name',)

class ListElementAdmin(admin.ModelAdmin):
    list_display = ('list', 'text', 'completed', 'show_element')
    search_fields = ('text', 'completed')

admin.site.register(List, ListAdmin)
admin.site.register(ListElement, ListElementAdmin)
