from django.urls import path
from .views import list_view,show_view,update_view,delete_view

urlpatterns = [
    path('lv/',list_view,name='list_url'),
    path('show/',show_view,name='show_url'),
    path('update/<int:pk>/',update_view,name='update_url'),
    path('delete/<int:pk>/',delete_view,name='delete_url')
]