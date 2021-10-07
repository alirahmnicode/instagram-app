# Generated by Django 3.2.7 on 2021-10-06 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0004_auto_20211006_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='profile',
        ),
        migrations.AddField(
            model_name='relation',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
