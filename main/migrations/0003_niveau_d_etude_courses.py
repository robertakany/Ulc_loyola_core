# Generated by Django 4.2.5 on 2023-11-10 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university_admin', '0001_initial'),
        ('main', '0002_niveau_d_etude_teachers'),
    ]

    operations = [
        migrations.AddField(
            model_name='niveau_d_etude',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='auditoire_courses', to='university_admin.course'),
        ),
    ]