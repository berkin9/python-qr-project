from django.urls import path, include

from rest_framework.routers import DefaultRouter

from main.api.views import BusinessViewSet, CustomUserViewSet, MenuViewSet, MenuItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r"profile", CustomUserViewSet, basename="profile")
router.register(r"business", BusinessViewSet, basename="business")
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"menuitem", MenuItemViewSet, basename="menuitem")

urlpatterns = [
    path("", include(router.urls), name="home"),
    # path('menu/<uuid:menu_pk>', api_views.MenuDetailAPIView.as_view()), doğrusu
    # path('category/', api_views.CategoryCreateAPIView.as_view()),
    # path('category/<int:cat_pk>', api_views.CategoryDetailAPIView.as_view()),
    # path('menuitem/', api_views.MenuItemCreateAPIView.as_view()),
    # path('menuitem/<int:item_pk>', api_views.MenuItemDetailAPIView.as_view()),

]
