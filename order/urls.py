from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.api.views import MenuViewSet, CategoryViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r"menu", MenuViewSet, basename="qr-menu")
router.register(r"category", CategoryViewSet, basename="qr-category")
router.register(r"menuitem", MenuItemViewSet, basename="qr-menuitem")

urlpatterns = [
    path("", include(router.urls), name="home"),
]
