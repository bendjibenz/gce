# Generated by Django 2.0 on 2018-04-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gce_app', '0009_copie_date_affichage'),
    ]

    operations = [
        migrations.AddField(
            model_name='anneescolaire',
            name='active',
            field=models.BooleanField(db_column='active_Scolaire', default=False, unique=True),
        ),
    ]