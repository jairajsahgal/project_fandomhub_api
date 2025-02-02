"""Routers for News App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import NewViewSet


router_v1 = DefaultRouter()
router_v1.register(r"news", NewViewSet, basename="new")

urlpatterns = [path("api/v1/", include(router_v1.urls))]
