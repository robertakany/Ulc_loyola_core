# Generated by Django 5.1.2 on 2025-02-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_admin', '0010_alter_student_options_alter_souscription_sexe_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='souscription',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='souscription',
            name='document_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='faculty',
            field=models.CharField(choices=[('Philosophe', 'philosophie'), ('Faculté des Sciences et Technologies', 'Faculté des Sciences et Technologies'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires'), ('Sciences Sociales et gestion', 'Sciences Sociales et gestion'), ('Administration des Affaires - Business school', 'Administration des Affaires - Business school')], max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(choices=[('Philosophe', 'philosophie'), ('Faculté des Sciences et Technologies', 'Faculté des Sciences et Technologies'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires'), ('Sciences Sociales et gestion', 'Sciences Sociales et gestion'), ('Administration des Affaires - Business school', 'Administration des Affaires - Business school')], max_length=255, verbose_name='Faculté'),
        ),
    ]
