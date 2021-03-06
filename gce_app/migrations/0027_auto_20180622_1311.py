# Generated by Django 2.0 on 2018-06-22 13:11

from django.db import migrations, models
import gce_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('gce_app', '0026_auto_20180620_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichiercopie',
            name='emplacement_fichier',
            field=models.FileField(blank=True, db_column='emplacement_Fichier', null=True, upload_to=gce_app.models.copies_file_path),
        ),
        migrations.AlterField(
            model_name='fichiercorrection',
            name='emplacement_fichier',
            field=models.FileField(blank=True, db_column='emplacement_Fichier', null=True, upload_to=gce_app.models.corrections_file_path),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='avatar_utilisateur',
            field=models.FileField(db_column='Avatar', default='default/default_avatar.png', upload_to=gce_app.models.avatars_file_path),
        ),
    ]
