# Generated by Django 2.2.1 on 2019-10-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191020_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Address',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(blank=True, choices=[('NG', 'Nigeria'), ('GH', 'Ghana'), ('SA', 'South Africa'), ('UG', 'Uganda')], max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profession',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='images/profile_picture'),
        ),
    ]