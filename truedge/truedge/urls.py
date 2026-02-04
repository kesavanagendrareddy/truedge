"""
URL configuration for truedge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainapp import views
from userapp import views as user_views
from adminapp import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('collections/', views.collections, name='collections'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('userdashboard/', user_views.user_dashboard, name='user_dashboard'),
    path('userfooter/', user_views.user_footer, name='user_footer'),
    path("admindashboard/",  admin_views.admin_dashboard, name="admin_dashboard"),
    path("products/", admin_views.products, name="products"),
    path("products/edit/<int:pk>/", admin_views.edit_product, name="edit_product"),
    path("products/delete/<int:pk>/", admin_views.delete_product, name="delete_product"),
    path("view_users/", admin_views.view_users, name="view_users"),
    path("adminlogin/", admin_views.admin_login, name="admin_login"),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
