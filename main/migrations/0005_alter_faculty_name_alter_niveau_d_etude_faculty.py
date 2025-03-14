# Generated by Django 5.1.2 on 2025-02-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_niveau_d_etude_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name',
            field=models.CharField(choices=[('Philosophe', 'philosophie'), ('Faculté des Sciences et Technologies', 'Faculté des Sciences et Technologies'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires'), ('Sciences Sociales et gestion', 'Sciences Sociales et gestion'), ('Administration des Affaires - Business school', 'Administration des Affaires - Business school')], max_length=100),
        ),
        migrations.AlterField(
            model_name='niveau_d_etude',
            name='faculty',
            field=models.CharField(choices=[('Philosophe', 'philosophie'), ('Faculté des Sciences et Technologies', 'Faculté des Sciences et Technologies'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires'), ('Sciences Sociales et gestion', 'Sciences Sociales et gestion'), ('Administration des Affaires - Business school', 'Administration des Affaires - Business school')], max_length=50, verbose_name='Faculté'),
        ),
    ]
