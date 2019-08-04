from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, 
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('<slug:category_slug>/', views.service_list,
         name='service_list_by_category'),
    path('<int:id>/<slug:slug>/', views.service_detail,
         name='servicem_detail'),
]