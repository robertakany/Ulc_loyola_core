# Generated by Django 4.2.5 on 2023-10-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_admin', '0012_souscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souscription',
            name='faculty',
            field=models.CharField(choices=[('Philosophie', 'philosophie'), ('Ingeniérie', 'Ingeniérie'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires')], max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('Philosophie', 'philosophie'), ('Ingeniérie', 'Ingeniérie'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires')], max_length=255),
        ),
    ]