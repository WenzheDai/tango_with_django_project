from django.contrib import admin
from rango.models import Category, Page, UserProfile

#user: Dai
#password: 123

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    preserve_filters = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
