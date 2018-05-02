# Generated by Django 2.0 on 2018-04-29 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gce_app', '0012_auto_20180427_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnneeUniv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee_univ', models.CharField(db_column='annee_Univ', max_length=500, null=True)),
                ('active', models.BooleanField(db_column='active_Univ', default=False)),
            ],
            options={
                'db_table': 'anneeUniv',
            },
        ),
        migrations.AlterField(
            model_name='copie',
            name='annee_copie',
            field=models.ForeignKey(blank=True, db_column='annee_Copie', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gce_app.AnneeUniv'),
        ),
        migrations.AlterField(
            model_name='correction',
            name='annee_correction',
            field=models.ForeignKey(blank=True, db_column='annee_Correction', null=True, on_delete=django.db.models.deletion.SET_NULL, to='gce_app.AnneeUniv'),
        ),
        migrations.DeleteModel(
            name='AnneeScolaire',
        ),
    ]