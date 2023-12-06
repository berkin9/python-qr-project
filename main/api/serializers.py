from rest_framework import serializers
from main.models import Business, Category, MenuItem, Menu, CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ["password"]
        # fields = "__all__"


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"
        # exclude = ['id', 'added_at', 'updated_at']


class MenuSerializer(serializers.ModelSerializer):
    Business = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Menu
        fields = "__all__"
        # exclude = ['id', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    Menu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
        # exclude = ['id']


class MenuItemSerializer(serializers.ModelSerializer):
    Category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = MenuItem
        fields = "__all__"
        #exclude = ['id']
