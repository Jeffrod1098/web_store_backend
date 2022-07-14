from django.urls import path

from web_store.models import Item
from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('items', views.ItemList.as_view(), name='item_list'),
    path('item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'),
]