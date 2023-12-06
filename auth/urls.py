
from django.urls import path
from auth.views import MyObtainTokenPairView, LogoutAllView, LogoutView, LogoutAPIView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenBlacklistView

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='auth_logout'),
    #path('logout_all/', LogoutAllView.as_view(), name='auth_logout_all'),

]