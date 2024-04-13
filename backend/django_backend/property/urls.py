from django.urls import path
from . import api

urlpatterns = [
    path('', api.properties_list, name='api_properties_list'),
    path('create/', api.create_property, name='api_create_property'),
    path('<uuid:pk>/', api.properties_detail, name='properties_detail'),
    path('<uuid:pk>/book/', api.book_property, name='properties_book'),
    path('<uuid:pk>/reservations/', api.reservation_list, name='reservations_list'),
    path('<uuid:pk>/toggle_favorite/', api.toggle_favorited, name='toggle_reservations'),
]