# Generated by Django 3.2.3 on 2021-07-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_myuser_usertype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateField(max_length=120, null=1),
        ),
    ]
