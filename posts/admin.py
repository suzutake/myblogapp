from django.contrib import admin

# Register your models here.
# from .models import Post

# Before register by admin screen, need to Import
from .models import MenuMaster, MenuDetail, Customer


#admin.site.register(Post)

#admin.site.register(Customer)
#admin.site.register(MenuMaster)
#admin.site.register(MenuDetail)

class MenuInLine(admin.StackedInline):
    model = MenuMaster
    extra = 4


class DetailInline(admin.TabularInline):
    model = MenuDetail
    extra = 3


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('Date information', {'fields': ['visitedDate']})
    ]
    inlines = [MenuInLine]

admin.site.register(Customer, CustomerAdmin)


class MenuMasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'customer_visitedDate', 'name')

    fieldsets = [
        ('customer', {'fields': ['customer']}),
        ('menu', {'fields': ['name']})
    ]

    def customer_visitedDate(self, obj):
        return obj.customer.visitedDate

    #inlines = [DetailInLine]

    #def nailst_name(self, obj):
    #    return obj.MenuDetail.nailist

admin.site.register(MenuMaster, MenuMasterAdmin)
