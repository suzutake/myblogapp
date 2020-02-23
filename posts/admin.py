from django.contrib import admin

# Register your models here.
from .models import Post

# Before register by admin screen, need to Import
from .models import MenuMaster
from .models import MenuDetail
from .models import Customer

admin.site.register(Post)

admin.site.register(Customer)
admin.site.register(MenuMaster)
admin.site.register(MenuDetail)
