"""myblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # for showing posts app
    path('posts/', include('posts.urls')),
    # for showing detail screen
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),

    #original show date_detail
    path('date/', views.date_detail, name='date_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # for showing picture by static file
