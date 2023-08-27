from django.urls import path
from .views import menu, remove_dish

urlpatterns = [
    path('menu/', menu, name='menu'),
    path('remove_dish/<int:dish_id>/', remove_dish, name='remove_dish')
]