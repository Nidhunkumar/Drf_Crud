from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_product, name='add_product'),
    path('all/', views.view_items, name='view_items'),
    path('update/<str:pk>/',views.update_items,name='update-items'),
    path('delete/<str:pk>/',views.delete_item,name='delete-item'),

]
