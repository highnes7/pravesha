# Generated by Django 2.1.7 on 2019-09-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_auto_20190919_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_aio_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_ar_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_bat_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_cert_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_mod_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_pp_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_pubg_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_reg_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_report_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_syt_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_th_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_tq_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='cs_ty_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_aio',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_ar',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_bat',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_mod',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_pp',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_pubg',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_syt',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_th',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_tq',
            field=models.CharField(default=None, max_length=4),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status_ty',
            field=models.CharField(default=None, max_length=4),
        ),
    ]
