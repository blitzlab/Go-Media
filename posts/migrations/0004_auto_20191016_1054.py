# Generated by Django 2.2.1 on 2019-10-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20191016_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(default='/images/gig.png', upload_to='images'),
        ),
    ]
