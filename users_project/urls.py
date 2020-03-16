"""users_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from users_app import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.index, name='index'),
    path('users/', users_views.users_list, name='users-list'),
    path('users/create', users_views.create_user, name='users-create'),
    path('users/update', users_views.update_user, name='users-update'),
    path('users/delete/<int:pk>', users_views.delete_user, name='users-delete'),
    path('login/', users_views.LogIn.as_view(), name='login'),
    path('logout/', users_views.logout_view, name='logout'),
    path('loggedin/', users_views.logged_in_view, name='loggedin'),
    path('shops/', include('shops.urls'))
]
