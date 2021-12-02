

from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home_view, name='homepage'),
    path('order_sandwich', views.sandwich_order_view, name='order_sandwich'),
    path('create_sandwich', views.create_sandwich_order_view, name='create_sandwich'),
    path('order_delete', views.sandwich_order_delete_view, name='delete_sandwich'),
    path('task_to_complete', views.task_to_complete_view, name='task_to_complete')
]