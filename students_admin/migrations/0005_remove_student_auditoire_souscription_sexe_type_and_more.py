# Generated by Django 4.2.5 on 2023-11-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_admin', '0004_rename_year_of_added_souscription_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='auditoire',
        ),
        migrations.AddField(
            model_name='souscription',
            name='sexe_type',
            field=models.CharField(default='', max_length=334),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='souscription',
            name='tuteur_email',
            field=models.EmailField(blank=True, max_length=234, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='tuteur_name',
            field=models.CharField(blank=True, max_length=234, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='tuteur_number',
            field=models.CharField(blank=True, max_length=234, null=True),
        ),
        migrations.DeleteModel(
            name='StudentCourses',
        ),
    ]
