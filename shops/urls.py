from django.urls import path
from shops import views

app_name = 'shops'

urlpatterns = [
    path('', views.shops, name='list'),
    path('create', views.shops_create, name='create'),
    path('update', views.shops_update, name='update'),
    path('delete/<int:pk>', views.shops_delete, name='delete'),
]