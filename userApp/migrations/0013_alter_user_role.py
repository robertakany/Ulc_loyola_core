# Generated by Django 4.2.5 on 2023-10-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0012_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('professeur', 'professeur'), ('etudiant', 'etudiant'), ('autres ', 'autres')], max_length=100),
        ),
    ]