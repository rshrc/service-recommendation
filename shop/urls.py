from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
    path('supports', views.support_page, name='support_page'),
    path('services-', views.service_render, name='service_render'),
    path('feedback', views.feedback_form, name='give_feedback'),
    path('service/purchased/', views.service_purchased, name='service_purchased'),
]
