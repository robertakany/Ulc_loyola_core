# Generated by Django 4.2.5 on 2023-11-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_new_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]