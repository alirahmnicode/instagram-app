# Generated by Django 3.2.7 on 2021-10-04 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-create',)},
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]