# Generated by Django 4.2 on 2023-04-25 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('admin_notes', models.TextField(blank=True, null=True, verbose_name='Admin Notes')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Added At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('customer_user_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_user_list', to=settings.AUTH_USER_MODEL, verbose_name='Customer User List')),
                ('root_user_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='root_user_list', to=settings.AUTH_USER_MODEL, verbose_name='Root User List')),
                ('staff_user_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff_user_list', to=settings.AUTH_USER_MODEL, verbose_name='Staff User List')),
            ],
            options={
                'verbose_name': 'Business',
                'verbose_name_plural': 'Businesses',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.CharField(blank=True, max_length=10, null=True, verbose_name='Price')),
                ('calorie', models.CharField(blank=True, max_length=10, null=True, verbose_name='Calorie')),
                ('allergens', models.CharField(blank=True, max_length=50, null=True, verbose_name='Allergens')),
                ('cook_level_available', models.BooleanField(default=False, verbose_name='Is Available?')),
                ('cook_level', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cook Level')),
                ('extra_list', models.CharField(blank=True, max_length=100, null=True, verbose_name='Extra List')),
                ('is_available', models.BooleanField(default=False, verbose_name='Is Available?')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='main.business', verbose_name='Business')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to='main.menu', verbose_name='Menu'),
        ),
    ]