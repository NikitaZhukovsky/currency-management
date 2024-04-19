# Generated by Django 5.0.4 on 2024-04-19 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name_plural': 'Currencies'},
        ),
        migrations.AddField(
            model_name='exchangesrate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='notification',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]