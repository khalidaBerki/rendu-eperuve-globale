# Generated by Django 5.0.6 on 2024-07-06 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResponsableLegal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Adherent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('adresse', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=20)),
                ('statut_cotisation', models.CharField(choices=[('Payée', 'Payée'), ('En attente', 'En attente'), ('Non payée', 'Non payée')], default='En attente', max_length=50)),
                ('badge_id', models.CharField(max_length=50, unique=True)),
                ('cours_id', models.IntegerField(blank=True, null=True)),
                ('responsable_legal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adherents.responsablelegal')),
            ],
        ),
    ]
