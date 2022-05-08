from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from starships import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'starships', views.StarshipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]