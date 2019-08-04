from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.recommend_view, name='get_recommend'),
]
