from rest_framework import serializers

from main.models import Menu, MenuItem, Category


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
        # exclude = ['id']
