from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'line', views.LineSet)


urlpatterns = [
    path('', views.index),
    path('api/', include(router.urls)),
    path('<str:model_name>/', views.list, name='list')
]