# Generated by Django 4.2.3 on 2023-07-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
