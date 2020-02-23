from django.contrib import admin

# Register your models here.
from .models import Post

# Before register by admin screen, need to Import
from .models import MenuMaster, MenuDetail, Customer


admin.site.register(Post)

admin.site.register(Customer)
#admin.site.register(MenuMaster)
admin.site.register(MenuDetail)


class DetailInline(admin.TabularInline):
    model = MenuDetail
    extra = 3


class MenuMasterAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['name']}),
    #    ('Date information', {'fields': ['visitedDate'], 'classes': ['collapse']}),
    #]
    inlines = [DetailInline]

admin.site.register(MenuMaster, MenuMasterAdmin)
