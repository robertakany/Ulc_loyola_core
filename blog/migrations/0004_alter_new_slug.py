# Generated by Django 4.2.5 on 2023-11-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_new_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
