# Generated by Django 2.1.7 on 2019-09-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20190905_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='Year',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]