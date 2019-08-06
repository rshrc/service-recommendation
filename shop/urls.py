from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('services', views.service_page, name='service_page'),
    path('supports', views.support_page, name='support_page'),
    path('service/purchased/', views.service_purchased, name='service_purchased'),
]
