# Generated by Django 4.2.5 on 2023-11-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_admin', '0003_studentcourses_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='souscription',
            old_name='year_of_added',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='souscription',
            name='registration_date',
        ),
        migrations.RemoveField(
            model_name='souscription',
            name='student',
        ),
        migrations.AddField(
            model_name='souscription',
            name='Place_of_birth',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='adress',
            field=models.CharField(blank=True, max_length=324, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='bithday',
            field=models.CharField(default='', max_length=345),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='souscription',
            name='common',
            field=models.CharField(blank=True, max_length=324, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='country',
            field=models.CharField(blank=True, max_length=324, null=True),
        ),
        migrations.AddField(
            model_name='souscription',
            name='email',
            field=models.EmailField(default='', max_length=233, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='souscription',
            name='level_of_study',
            field=models.CharField(choices=[('Baccalauréat', 'Baccalauréat'), ('Graduat', 'Graduat'), ('License', 'License'), ('Master', 'Master'), ('Doctorat', 'Doctorat')], default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='souscription',
            name='first_name',
            field=models.CharField(max_length=45, verbose_name='Prenom'),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='last_name',
            field=models.CharField(max_length=45, verbose_name='Nom de la famille'),
        ),
    ]