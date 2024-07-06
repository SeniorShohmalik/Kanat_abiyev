# Generated by Django 5.0 on 2024-01-31 14:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reyting',
            new_name='UReyting',
        ),
        migrations.RemoveField(
            model_name='savol',
            name='javoblar',
        ),
        migrations.RemoveField(
            model_name='test',
            name='savol',
        ),
        migrations.AddField(
            model_name='javoblar',
            name='savol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mytest.savol'),
        ),
        migrations.AddField(
            model_name='savol',
            name='test',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mytest.test'),
        ),
    ]