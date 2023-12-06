from django.core.exceptions import BadRequest
from rest_framework import mixins, request
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from main.models import Menu, MenuItem, Category
from order.api.serializers import MenuSerializer, MenuItemSerializer, CategorySerializer


# Create your views here.

class MenuViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  GenericViewSet):
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        if self.request.query_params.get("business_id"):
            return Menu.objects.filter(business=self.request.query_params.get("business_id"))
        else:
            raise BadRequest("business_id nerede")
            # return None
            # raise PermissionDenied()
            # return Response(data="Business id",status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    # def get_queryset(self):
    #     if self.request.query_params.get("business_id"):
    #         return Category.objects.filter(business=self.request.query_params.get("business_id"))
    #     else:
    #         raise BadRequest("business_id nerede")
    def get_queryset(self):
        return Category.objects.filter(menu__business__staff_user_list__in=[self.request.user.id, ])


class MenuItemViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # return MenuItem.objects.filter(category__menu__business__customer_user_list=self.request.user.id)
        return MenuItem.objects.filter(category__menu__business__staff_user_list_in=[self.request.user.id, ])
