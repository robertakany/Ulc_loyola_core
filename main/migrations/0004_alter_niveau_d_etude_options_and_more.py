# Generated by Django 5.1.2 on 2025-02-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_niveau_d_etude_courses'),
        ('teachers_admin', '0002_alter_teacher_options_alter_teacher_born_date_and_more'),
        ('university_admin', '0003_alter_course_options_alter_studentcourses_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='niveau_d_etude',
            options={'verbose_name': "Niveau d'etudes", 'verbose_name_plural': "Niveau d'etudes"},
        ),
        migrations.AlterField(
            model_name='niveau_d_etude',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='auditoire_courses', to='university_admin.course', verbose_name='cours'),
        ),
        migrations.AlterField(
            model_name='niveau_d_etude',
            name='faculty',
            field=models.CharField(choices=[('Philosophie', 'philosophie'), ('Ingeniérie', 'Ingeniérie'), ('Agronomiques et Vetérinaires', 'Agronomiques et Vetérinaires'), ('Général', 'Général')], max_length=50, verbose_name='Faculté'),
        ),
        migrations.AlterField(
            model_name='niveau_d_etude',
            name='teachers',
            field=models.ManyToManyField(blank=True, related_name='auditoire_teachers', to='teachers_admin.teacher', verbose_name='Proffesseurs'),
        ),
    ]
