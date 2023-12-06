from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import uuid


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, verbose_name=("Email address"))
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=("Phone"))
    # avatar = models.ImageField(upload_to=avatar_upload, blank=True, null=True, verbose_name=_("Avatar"))
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name=("Address"))
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=("Country"))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=("City"))
    admin_notes = models.TextField(blank=True, null=True, verbose_name=("admin.notes"))
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = ["email", "first_name", "last_name"]
    is_blocked = models.BooleanField(default=False, verbose_name=("Is Blocked?"))


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Address"))
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Country"))
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("City"))
    admin_notes = models.TextField(blank=True, null=True, verbose_name=_("Admin Notes"))
    root_user_list = models.ManyToManyField(CustomUser, blank=True, null=True, related_name='root_user_list',
                                            verbose_name=_("Root User List"))
    customer_user_list = models.ManyToManyField(CustomUser, blank=True, null=True, related_name='customer_user_list',
                                                verbose_name=_("Customer User List"))
    staff_user_list = models.ManyToManyField(CustomUser, blank=True, null=True, related_name='staff_user_list',
                                             verbose_name=_("Staff User List"))
    # license = models.ForeignKey(License, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("License"),related_name='license')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Added At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    # logo = models.ImageField(upload_to=business_logo_upload, blank=True, null=True, verbose_name=_("Logo"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Business")
        verbose_name_plural = _("Businesses")
        ordering = ['name']


class Menu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Business"),
                                 related_name='business')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Menu"),
                             related_name='menu')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Category"),
                                 related_name='category')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Name"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Description"))
    price = models.CharField(max_length=10, blank=True, null=True, verbose_name=_("Price"))
    # photo = models.ImageField(upload_to=menuitem_photo_upload, blank=True, null=True, verbose_name=_("Logo"))
    calorie = models.CharField(max_length=10, blank=True, null=True, verbose_name=_("Calorie"))
    allergens = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Allergens"))
    cook_level_available = models.BooleanField(default=False, verbose_name=("Is Available?"))#CHANGABLE COOK LEVEL
    cook_level = models.CharField(max_length=20, blank=True, null=True, verbose_name=_("Cook Level"))
    extra_list = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Extra List"))
    is_available = models.BooleanField(default=False, verbose_name=("Is Available?"))

    def __str__(self):
        return self.name
