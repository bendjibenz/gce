# Generated by Django 2.0 on 2018-04-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gce_app', '0005_reclamation_regler_reclamation'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultation',
            name='approve_consultation',
            field=models.BooleanField(db_column='approve_Consultation', default=False),
        ),
    ]