# Generated by Django 3.2.3 on 2021-07-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_auto_20210719_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='usertype',
            field=models.CharField(max_length=50, null=1),
            preserve_default=1,
        ),
    ]
