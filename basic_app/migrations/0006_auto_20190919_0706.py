# Generated by Django 2.1.7 on 2019-09-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20190919_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_aio',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_ar',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_bat',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_mod',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_pp',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_pubg',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_syt',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_th',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_tq',
            field=models.CharField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_ty',
            field=models.CharField(default=0, max_length=4),
        ),
    ]
