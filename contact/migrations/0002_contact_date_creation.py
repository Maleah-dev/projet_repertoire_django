# Generated by Django 4.1.2 on 2022-11-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_creation',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
