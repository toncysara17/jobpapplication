# Generated by Django 3.2.3 on 2021-07-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0005_auto_20210719_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=120, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.CharField(max_length=100, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='job',
            name='experience',
            field=models.CharField(max_length=120, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(null=1, upload_to=''),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=120, null=1),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='job',
            name='phone',
            field=models.CharField(max_length=12, null=1),
            preserve_default=1,
        ),
    ]