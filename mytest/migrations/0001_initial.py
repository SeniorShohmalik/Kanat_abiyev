# Generated by Django 5.0 on 2024-01-30 11:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Javoblar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javob', models.CharField(max_length=255)),
                ('qiymat', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Savol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.ImageField(upload_to='savol_images/')),
                ('savol', models.CharField(max_length=255)),
                ('javoblar', models.ManyToManyField(to='mytest.javoblar')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
                ('savol', models.ManyToManyField(to='mytest.savol')),
            ],
        ),
        migrations.CreateModel(
            name='Reyting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('natija', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foydalanuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mytest.test')),
            ],
        ),
    ]
