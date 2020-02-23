from django.contrib import admin

# Register your models here.
# from .models import Post

# Before register by admin screen, need to Import
from .models import MenuMaster, MenuDetail, Customer


#admin.site.register(Post)


class MenuInLine(admin.StackedInline):
    model = MenuMaster
    extra = 4


class DetailInline(admin.StackedInline):
    model = MenuDetail
    extra = 3


class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('name', {'fields': ['name']}),
        ('Date information', {'fields': ['visitedDate']})
    ]
    inlines = [MenuInLine]

admin.site.register(Customer, CustomerAdmin)


#class MenuMasterAdmin(admin.ModelAdmin):
    #list_display = ('id', 'customer', 'customer_visitedDate', 'name','nailist_name')
#    list_display = ('id', 'customer', 'customer_visitedDate', 'name')
#    list_display_links = ['id', 'customer', 'name']

#    fieldsets = [
#        ('customer', {'fields': ['customer']}),
#        ('menu', {'fields': ['name']})
#    ]

#    def customer_visitedDate(self, obj):
#        return obj.customer.visitedDate

#    def nailist_name(self, obj):
#        return obj.MenuDetail.nailist

#    inlines = [DetailInline]


#admin.site.register(MenuMaster, MenuMasterAdmin)

class MenuDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'nailist','money')
    list_display_links = ['name','nailist']

    fieldsets = [
        #('customer', {'fields': ['customer']}),
        ('menu', {'fields': ['name']}),
        ('nailist',{'fields': ['nailist']}),
        ('money',{'fields': ['money']})
    ]
    #fields = ['id', 'name', 'nailist','money']

    def customer(self, obj):
        return obj.name.customer

admin.site.register(MenuDetail, MenuDetailAdmin)
