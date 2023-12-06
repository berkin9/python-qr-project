from pickle import GET

from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from main.api.serializers import BusinessSerializer, CategorySerializer, MenuItemSerializer, MenuSerializer, \
    CustomUserSerializer
from main.models import Business, Category, MenuItem, Menu, CustomUser
from main.api.permissions import IsSuperUser, IsOwnPermission


class CustomUserViewSet(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        GenericViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)


class BusinessViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,  # delete butonu,
                      GenericViewSet):
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Business.objects.filter(customer_user_list__id=self.request.user.id).order_by("added_at")
        return Business.objects.filter(staff_user_list__id__in=[self.request.user.id, ]).order_by("added_at")
    # TODO: Farkı


class MenuViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,  # delete butonu,
                  GenericViewSet):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Menu.objects.all()
        return Menu.objects.filter(business__staff_user_list__in=[self.request.user.id, ])


class CategoryViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,  # delete butonu,
                      GenericViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Category.objects.all()
        # return Category.objects.filter(menu__business__customer_user_list=self.request.user.id)
        return Category.objects.filter(menu__business__staff_user_list__in=[self.request.user.id, ])


class MenuItemViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,  # delete butonu,
                      GenericViewSet):
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MenuItem.objects.filter(category__menu__business__customer_user_list__in=[self.request.user.id, ])


# return MenuItem.objects.filter(category__menu__business_id__in=self.request.user.id) and MenuItem.objects.filter(
# category__menu=self.request.user.id)


class BusinessCreateAPIView(generics.ListCreateAPIView):
    queryset = Business.objects.all().order_by('id')
    serializer_class = BusinessSerializer
    permission_classes = [IsAuthenticated]


class BusinessDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    # permission_classes = [IsAdminUserOrReadOnly]


class MenuCreateAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all().order_by('id')
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [IsYorumSahibiOrReadOnly]


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsYorumSahibiOrReadOnly]


class MenuItemCreateAPIView(generics.CreateAPIView):
    queryset = MenuItem.objects.all().order_by('id')
    serializer_class = MenuItemSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MenuItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    # permission_classes = [IsYorumSahibiOrReadOnly]

    def perform_create(self, serializer):
        item_pk = self.kwargs.get('item_pk')  # urlden kitap_pk parametresini çekme
        item = get_object_or_404(MenuItem, id=item_pk)  # böyle kitap varsa çektik
        kullanici = self.request.user
        items = MenuItem.objects.filter(id=item_pk)  # yorumu sahibine göre filtreledi.
