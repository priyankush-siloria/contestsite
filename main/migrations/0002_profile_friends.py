# Generated by Django 2.0.2 on 2018-03-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.TextField(blank=True, null=True),
        ),
    ]
