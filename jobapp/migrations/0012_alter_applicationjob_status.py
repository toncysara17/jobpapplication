# Generated by Django 3.2.3 on 2021-07-23 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0011_alter_applicationjob_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationjob',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Reject', 'Reject'), ('Approve', 'Approve')], default='Pending', max_length=120),
        ),
    ]